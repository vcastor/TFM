###########################################
### E_{HB} vs E_{int}^{\mathrm{H_2O}\cdots\mathrm{H_2O}^{\,\prime}
###########################################

from pylab import *
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import math
import pylab
import matplotlib.ticker as ticker

#### Imprimir como antes
# import matplotlib.style
# import matplotlib as mpl
# mpl.style.use('classic')
####

###########################################
### Dibujos de graficas
###########################################

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()
ax1 = fig.add_subplot(111)

for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

###########################################
### E_{HB} estimated
###########################################

x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#G:y = [-13.313, -11.232, -11.083, -10.338, -9.693, -9.356, -8.905, -8.299, -7.803, -7.116]
#G:e = [1.315, 1.317, 0.676, 0.384, 1.029, 0.960, 1.347, 2.131, 0.765, 1.236]
y = [-15.077, -11.716, -11.327, -10.440, -9.610, -9.091, -8.605, -7.875, -7.147, -6.466]
e = [2.255, 1.905, 0.953, 0.299, 1.349, 1.217, 1.727, 2.169, 0.833, 1.235]

plt.errorbar(x,y, yerr=e, color='red', marker='o',
             label=r'$E_{\mathrm{HB}}$ estimaci\'{o}n Espinosa')


###########################################
### Escala de Castor 2020
###########################################

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-5.804, -6.165, -6.410, -6.947, -6.927, -7.340, -7.829, -8.570, -8.692, -9.551]
e = [0.912, 0.458, 1.088, 0.524, 0.575, 0.633, 0.035, 0.329, 0.660, 0.551]

plt.errorbar(x,y, yerr=e, color='blue', marker='o',
             label=r'$E_{\mathrm{int}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}^{ \, \prime}}$ en este trabajo')


###########################################
### Espacio de dibujo
###########################################

plt.xlim((0.5, 10.5))
plt.ylim((-18.0, -4.0))

###########################################
### Graducion de ejes
###########################################
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

###########################################
### Notas
###########################################

#plt.title('New vs old scale')
leg = ax1.legend(loc='lower left')
ax1.set_xlabel('Tipo de EH')
ax1.set_ylabel(r'$E$ $(\mathrm{kcalmol^{-1}})$')


###########################################
### Imprimir
###########################################

plt.show()
fig.savefig('EHB_vs_Eint.pdf')








