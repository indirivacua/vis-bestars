from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
import seaborn as sns
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

from matplotlib.colors import LogNorm
import math

def correlation_matrix(df, columns):
    corr_matrix = df[columns].corr().abs()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    # Apply logarithmic color map
    log_norm = LogNorm(vmin=corr_matrix.min().min(), vmax=corr_matrix.max().max())
    sns.heatmap(corr_matrix, mask=mask, cmap=cmap, norm=log_norm, 
               vmax=1, vmin=-1, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

def violin(df, columns):
    sns.violinplot(data=df[columns], inner="points")    
    plt.tight_layout()
    plt.show()

def histogram(df, columns):
    cmaps = sns.color_palette(as_cmap=True)

    axes = df[columns].hist(bins=15)

    for i, ax in enumerate(axes.flatten()):
        for rect in ax.patches:
            rect.set_color(cmaps[i % len(cmaps)])

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
    scatter_matrix = pd.plotting.scatter_matrix(df[columns],alpha=0.9,grid=False)

    cmaps = sns.color_palette(as_cmap=True)

    # Cambia el color de los títulos de los ejes
    for ax in scatter_matrix.ravel():
        ax.xaxis.label.set_color(cmaps[columns.index(ax.xaxis.label.get_text())])
        ax.yaxis.label.set_color(cmaps[columns.index(ax.yaxis.label.get_text())])

    plt.show()

from astropy.coordinates import SkyCoord
import astropy.units as u
def sky_cord(df, columns):
    global name
    name = None
    column_selector(df)
    if name == None: #user cancel
        return

    # Crear un mapa de colores para los tipos de estrellas
    unique_stars = df[name].unique()
    colors = ('#556270','#4ECDC4','#C7F464', '#000000')
    colormap = {star: color for star, color in zip(unique_stars, colors)}

    # Mapear los tipos de estrellas a colores
    df['color'] = df[name].map(colormap)

    # Convertir las coordenadas RA y DEC a objetos SkyCoord
    coords = SkyCoord(df[columns[0]], df[columns[1]], unit=(u.hourangle, u.deg))

    # Crear un gráfico del cielo
    plt.figure(figsize=(10, 6))
    for star in unique_stars:
        plt.scatter(coords.ra[df[name] == star], coords.dec[df[name] == star], marker='o', alpha=0.5, label=star, c=df['color'][df[name] == star])
    plt.xlabel(f'Ascensión Recta ({columns[0]})')
    plt.ylabel(f'Declinación ({columns[1]})')
    plt.title('Ubicaciones de Estrellas Be en el Cielo')
    plt.legend()
    plt.grid(True)
    plt.show()