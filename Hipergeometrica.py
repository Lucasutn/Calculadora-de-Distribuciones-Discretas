#paneles
import math
import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()
application_window.withdraw()


#tabla
from tabulate import tabulate

# importando modulos necesarios
#%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
#import seaborn as sns

np.random.seed(2016) # replicar random





# Ingreso de datos
N=int(simpledialog.askstring("Distribucion Hipergeometrica", "Ingrese el valor de N : ",
                                parent=application_window))

X=float(simpledialog.askstring("Distribucion Binomial", "Ingrese el valor de X : ",
                                parent=application_window))
n=float(simpledialog.askstring("Distribucion Binomial", "Ingrese el valor de N : ",
                                parent=application_window))

# N, x, n = 10, 4, 5 # parametros de forma

hipergeometrica = stats.hypergeom(N, X, n) # Distribución
x = np.arange(0, X+1)
fmp = hipergeometrica.pmf(x) # Función de Masa de Probabilidad




plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Hipergeométrica')
plt.ylabel('probabilidad')
plt.xlabel('valores')




print(tabulate({"x": x,"p": fmp}, headers="keys"))
plt.show()