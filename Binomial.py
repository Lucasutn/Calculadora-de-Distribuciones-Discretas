#paneles
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

Vx = np.arange(binomial.ppf(0),
              binomial.ppf(1))
Ex=binomial.pmf(Vx)

fmp = binomial.pmf(x) # Función de Masa de Probabilidad



plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')

print("V(x)= " + str((np.var(Ex)*1000)) )
print("E(x)= " + str((np.median(Ex)*1000)) )


print(tabulate({"x": x,"p": fmp}, headers="keys"))

plt.show()

# x = np.arange(binomial.ppf(0.0),
#               binomial.ppf(1))

