from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.main_window import Ui_MainWindow
import sys
import csv
import pandas as pd
import numpy as np
from visualizations import *

df = None

def find_checked(treeWidget):
    checked = dict()
    root = treeWidget.invisibleRootItem()
    signal_count = root.childCount()

    for i in range(signal_count):
        signal = root.child(i)
        checked_sweeps = list()
        num_children = signal.childCount()

        for n in range(num_children):
            child = signal.child(n)

            if child.checkState(0) == Qt.Checked:
                checked_sweeps.append(child.text(0))

        checked[signal.text(0)] = checked_sweeps

    return checked

def generate_custom_message_box(title: str, text: str, icon: QMessageBox.Icon = QMessageBox.Critical):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(icon)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)
    msg.exec_()

def get_file():
    filename, _filter = QFileDialog.getOpenFileName(MainWindow, 'Open file', '', 'CSV files (*.csv)')
    ui.lineEdit_filepath.setText(filename)

    # Fill TableView
    with open(filename, "r") as fileInput:
        for i, row in enumerate(csv.reader(fileInput)):
            if i == 0:
                model.setHorizontalHeaderLabels([r.strip().strip('"') for r in row])
            else:
                items = [
                    QStandardItem(field.strip())
                    for field in row
                ]
                model.appendRow(items)
    
    global df
    df = pd.read_csv(filename)

    # Fill TreeWidget
    parent = QTreeWidgetItem(ui.treeWidget_features)
    parent.setText(0, "Atributos")
    parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
    for x, d in zip(df.columns, df.dtypes):
        child = QTreeWidgetItem(parent)
        child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
        child.setText(0, "{} ({})".format(x, d))
        child.setCheckState(0, Qt.Unchecked)
    
    ui.pushButton_vis.setEnabled(True)

def generate_visualization():
    df_local = df
    if ui.radioButton_remove_tuples.isChecked():
        df_local = df.dropna()
    elif ui.radioButton_fill_mean.isChecked():
        df_local = df.fillna(df.mean(numeric_only=True))

    vis_selection = ui.comboBox_vis.currentText()

    columns = find_checked(ui.treeWidget_features)
    columns = columns["Atributos"]
    columns = [x.split(' ')[0] for x in columns] #remove the type

    try:
        if vis_selection == "Matriz de correlación":
            correlation_matrix(df_local, columns)
        else:
            generate_custom_message_box(
                "Error: Not Implemented", 
                "La visualización no se encuentra implementada aún.")
    except Exception as e:
        generate_custom_message_box("Error: Visualization can't be shown.", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Setup UI

    ui.pushButton_vis.setEnabled(False)
    ui.lineEdit_filepath.setReadOnly(True)
    ui.pushButton_file.clicked.connect(get_file)
    ui.pushButton_vis.clicked.connect(generate_visualization)

    model = QStandardItemModel()
    ui.tableView_dataframe.setModel(model)
    ui.tableView_dataframe.horizontalHeader().setStretchLastSection(True)

    vis_options = [
        "Histograma", 
        "Diagrama de dispersión", 
        "Matriz de correlación", 
        "Diagrama de violín", 
        "Mapa de calor", 
        "Gráfico de coordenadas paralelas", 
        "Visualización en el cielo"
        ]

    ui.comboBox_vis.addItems(vis_options)

    MainWindow.show()
    sys.exit(app.exec_())
