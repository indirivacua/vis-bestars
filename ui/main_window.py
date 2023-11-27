# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowSKdSes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(777, 540)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_filepath = QLineEdit(self.frame)
        self.lineEdit_filepath.setObjectName(u"lineEdit_filepath")

        self.horizontalLayout.addWidget(self.lineEdit_filepath)

        self.pushButton_file = QPushButton(self.frame)
        self.pushButton_file.setObjectName(u"pushButton_file")

        self.horizontalLayout.addWidget(self.pushButton_file)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableView_dataframe = QTableView(self.frame_4)
        self.tableView_dataframe.setObjectName(u"tableView_dataframe")

        self.horizontalLayout_2.addWidget(self.tableView_dataframe)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_fill_mean = QRadioButton(self.groupBox)
        self.radioButton_fill_mean.setObjectName(u"radioButton_fill_mean")
        self.radioButton_fill_mean.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_fill_mean)

        self.radioButton_remove_tuples = QRadioButton(self.groupBox)
        self.radioButton_remove_tuples.setObjectName(u"radioButton_remove_tuples")

        self.horizontalLayout_3.addWidget(self.radioButton_remove_tuples)


        self.verticalLayout.addWidget(self.groupBox)

        self.comboBox_vis = QComboBox(self.frame_2)
        self.comboBox_vis.setObjectName(u"comboBox_vis")

        self.verticalLayout.addWidget(self.comboBox_vis)

        self.treeWidget_features = QTreeWidget(self.frame_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_features.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_features.setObjectName(u"treeWidget_features")

        self.verticalLayout.addWidget(self.treeWidget_features)

        self.pushButton_vis = QPushButton(self.frame_2)
        self.pushButton_vis.setObjectName(u"pushButton_vis")

        self.verticalLayout.addWidget(self.pushButton_vis)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 777, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Herramienta de Visualizaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Herramienta de Visualizaci\u00f3n para Datos Astron\u00f3micos (Be stars)</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Autores: Oscar Agust\u00edn Stanchi y Santiago Ponte Ahon</span></p></body></html>", None))
        self.pushButton_file.setText(QCoreApplication.translate("MainWindow", u"Cargar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tratamiento de los valores faltantes", None))
        self.radioButton_fill_mean.setText(QCoreApplication.translate("MainWindow", u"Rellenar con la media", None))
        self.radioButton_remove_tuples.setText(QCoreApplication.translate("MainWindow", u"Eliminar las tuplas", None))
        self.pushButton_vis.setText(QCoreApplication.translate("MainWindow", u"Visualizar", None))
    # retranslateUi

