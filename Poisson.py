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




# Graficando Poisson

# Ingreso de datos

mu=float(simpledialog.askstring("Distribución Poisson", "Ingrese el valor de p : ",
                                parent=application_window))
#mu =  2.4 # parametro de forma
poisson = stats.poisson(mu) # Distribución
x = np.arange(poisson.ppf(0.01),
              poisson.ppf(0.9999))
fmp = poisson.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Poisson')
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

xV = (Vx-(math.pow(Ex,2)))

print("D(x) = " + str(math.sqrt(xV)))



print(tabulate({"x": x,"p": fmp,"Xi * P(x)":lista_Ex,"Xi ^2 * P(x)":lista_Vx}, headers="keys"))


plt.show()