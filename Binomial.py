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
N, p = 20, 0.3 # parametros de forma
binomial = stats.binom(N, p) # Distribución
x = np.arange(binomial.ppf(0.01),
              binomial.ppf(0.99))
fmp = binomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()