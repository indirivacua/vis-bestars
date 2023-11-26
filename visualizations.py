import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

def correlation_matrix(df, columns):
    corr_matrix = df[columns].corr().abs()
    sn.heatmap(corr_matrix)
    plt.show()
