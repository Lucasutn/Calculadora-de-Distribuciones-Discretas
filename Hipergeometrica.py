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

X=float(simpledialog.askstring("Distribucion Hipergeometrica", "Ingrese el valor de X : ",
                                parent=application_window))
n=float(simpledialog.askstring("Distribucion Hipergeometrica", "Ingrese el valor de N : ",
                                parent=application_window))

# N, x, n = 10, 4, 5 # parametros de forma

hipergeometrica = stats.hypergeom(N, X, n) # Distribución
x = np.arange(0, n+1)
fmp = hipergeometrica.pmf(x) # Función de Masa de Probabilidad




plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Hipergeométrica')
plt.ylabel('probabilidad')
plt.xlabel('valores')

# Varianza y Ex

Ex=0
lista_Ex = list(map(lambda x,y: x*y, x, fmp))


for l in lista_Ex:
    Ex=Ex+l




xi2 = list(map(lambda x,y: x*y, x, x))


Vx=0
lista_Vx = list(map(lambda x,y: x*y, xi2, fmp))

for l in lista_Vx:
    Vx=Vx+l

print("Varianza = "+ str(Vx-(math.pow(Ex,2))))
print("Esperanza = "+ str(Ex))

xV = (Vx - (math.pow(Ex, 2)))

print("D(x) = " + str(math.sqrt(xV)))


print(tabulate({"x": x,"p": fmp,"Xi * P(x)":lista_Ex,"Xi ^2 * P(x)":lista_Vx}, headers="keys"))

plt.show()