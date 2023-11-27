from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

name = None

def column_selector(dataset):
    window = QDialog()
    window.setWindowTitle("Seleccionar una columna")
    layout = QGridLayout()
    label = QLabel("Elige una columna del dataset:")
    layout.addWidget(label, 0, 0, 1, 5) # Añadir la etiqueta a la primera fila, abarcando las 5 columnas
    buttons = []
    row = 1
    col = 0
    for column in dataset.columns:
        button = QRadioButton(column)
        layout.addWidget(button, row, col)
        buttons.append(button)
        col += 1
        if col == 5:
            col = 0
            row += 1
    row += 1 # Agregar una fila adicional antes del botón "Aceptar"
    accept = QPushButton("Aceptar")
    accept.clicked.connect(lambda: set_name(window, buttons))
    layout.addWidget(accept, row, 0, 1, 5) # Añadir el botón de aceptar a la última fila, abarcando las 5 columnas
    window.setLayout(layout)
    window.exec_()

def set_name(window, buttons):
    global name
    for button in buttons:
        if button.isChecked():
            name = button.text()
            break
    window.close()

def correlation_matrix(df, columns):
    corr_matrix = df[columns].corr().abs()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    # Generate a custom diverging colormap
    cmap = sn.diverging_palette(230, 20, as_cmap=True)
    sn.heatmap(corr_matrix, mask=mask, cmap=cmap, 
               vmax=1, vmin=-1, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

def violin(df, columns):
    sn.violinplot(data=df[columns], inner="points")    
    plt.tight_layout()
    plt.show()

def histogram(df, columns):
    df[columns].hist(bins=15)
    plt.show()

def parallel_coordinates(df, columns):
    global name
    name = None
    column_selector(df)
    if name == None: #user cancel
        return
    xy = pd.concat([df[columns],df[name]],axis=1)
    pd.plotting.parallel_coordinates(xy,name,color=('#556270','#4ECDC4','#C7F464', '#000000'))
    plt.show()

def scatter_matrix(df, columns):
    pd.plotting.scatter_matrix(df[columns],alpha=0.9,grid=False)
    plt.show()

from astropy.coordinates import SkyCoord
import astropy.units as u
def sky_cord(df, columns):
    # Convertir las coordenadas RA y DEC a objetos SkyCoord
    coords = SkyCoord(df[columns[0]], df[columns[1]], unit=(u.hourangle, u.deg))

    # Crear un gráfico del cielo
    plt.figure(figsize=(10, 6))
    plt.scatter(coords.ra, coords.dec, marker='o', alpha=0.5, label='Estrellas Be')
    plt.xlabel(f'Ascensión Recta ({columns[0]})')
    plt.ylabel(f'Declinación ({columns[1]})')
    plt.title('Ubicaciones de Estrellas Be en el Cielo')
    plt.legend()
    plt.grid(True)
    plt.show()