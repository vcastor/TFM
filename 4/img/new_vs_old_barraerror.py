###########################################
### Escala 2016 vs 2020 con barras de error
###########################################

from pylab import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import math
import pylab
import matplotlib.ticker as ticker

#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')
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
### Escala de Toche PCCP 2016
###########################################

#x = [10, 7, 6, 3, 2, 1]
x = [1, 4, 5, 8, 9, 10]
y = [-5.2166666667, -7.0125, -6.965, -9.1166666667, -9.25, -9.6533333333]
e = [0.75627376, 0.489569782, 0.1909188309, 0.3499285641, 0.6158246504, 0.6046762219]

plt.errorbar(x,y, yerr=e, color='red', marker='o',
             label=r'$E_{\mathrm{int}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}^{ \, \prime}}$ Escala 2016')


###########################################
### Escala de Castor 2020
###########################################

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-5.804, -6.165, -6.410, -6.947, -6.927, -7.340, -7.829, -8.570, -8.692, -9.551]
e = [0.912, 0.458, 1.088, 0.524, 0.575, 0.633, 0.035, 0.329, 0.660, 0.551]

plt.errorbar(x,y, yerr=e, color='blue', marker='o',
             label=r'$E_{\mathrm{int}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}^{ \, \prime}}$ Escala 2020')


###########################################
### Espacio de dibujo
###########################################

plt.xlim((0.5, 10.5))
plt.ylim((-11.0, -4.0))

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
ax1.set_ylabel(r'$E_{\mathrm{int}}^{ \, \prime} (\mathrm{kcalmol^{-1}}$)')


###########################################
### Imprimir
###########################################

plt.show()
fig.savefig('New_vs_old_barraerror.pdf')








