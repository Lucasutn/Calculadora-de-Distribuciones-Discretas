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

# parametros esteticos de seaborn
#sns.set_palette("deep", desat=.6)
#sns.set_context(rc={"figure.figsize": (8, 4)})



# Graficando Binomial
#n, p = 20, 0.3 # parametros de forma

#print("Distribucion Binomial\n")

#print("Ingrese el valor de n: ")
#n=int(input())
# print("Ingrese el valor de p: ")
# p=float(input())


n=int(simpledialog.askstring("Distribucion Binomial", "Ingrese el valor de n: ",
                                parent=application_window))

p=float(simpledialog.askstring("Distribucion Binomial", "Ingrese el valor de p: ",
                                parent=application_window))



binomial = stats.binom(n, p) # Distribución



x = np.arange(binomial.ppf(0.0001),
              binomial.ppf(0.99))



fmp = binomial.pmf(x) # Función de Masa de Probabilidad


img = plt.imread("pp.png")
# fig, ax = plt.subplots()
# x = range(300)
# ax.imshow(img, extent=[0, 400, 0, 300])
# ax.plot(x, x, '--', linewidth=5, color='firebrick')

plt.plot(x, fmp, '--',linewidth=1, color='firebrick')
plt.imshow(img,aspect="auto",extent=[0, 10, 0, 1],alpha=0.6)
plt.vlines(x, 0, fmp, colors='black', lw=20, alpha=0.8)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')

# Varianza y Esperanza

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

# x = np.arange(binomial.ppf(0.0),
#               binomial.ppf(1))

