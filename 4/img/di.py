###########################################
### Escala de DI con barras de erro
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
### Escala de DI
###########################################

x=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.2336, 0.2032, 0.1957, 0.1902, 0.1815, 0.1753, 0.1659, 0.1614, 0.1507, 0.1413]
e = [0.0192, 0.0171, 0.0098, 0.0063, 0.0162, 0.0126, 0.0186, 0.0165, 0.0105, 0.0174]

plt.errorbar(x,y, yerr=e, color='red', marker='o',
             label='DI')


###########################################
### Espacio de dibujo
###########################################

plt.xlim((0.5, 10.5))
plt.ylim((0.10, 0.26))

###########################################
### Graducion de ejes
###########################################
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

###########################################
### Notas
###########################################

#plt.title('New vs old scale')
#leg = ax1.legend(loc='lower left')
ax1.set_xlabel('Tipo de EH')
ax1.set_ylabel('Indice de Deslocalizacion')


###########################################
### Imprimir
###########################################

plt.show()
fig.savefig('DI.pdf')








