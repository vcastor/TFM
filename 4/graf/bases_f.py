##############################################
### Bases y Funcionales
###############################################

from pylab import *
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import math
import pylab
import matplotlib.ticker as ticker


###############################################
### Dibujaremos
###############################################

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()
ax1 = fig.add_subplot(111)

for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))


###############################################
## Data
###############################################

#Read the first file
x  = []
y = []
x1 = []

archivo = open('bases_f.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = str(columns[0]), float(columns[1])
    x.append(str(columns[0]))
    y.append(float(columns[1]))
archivo.close()

###############################################
### Convierte los nombres a numeros para plotear
###############################################

x1 = np.arange(len(x))


###############################################
### Espacio de dibujo
###############################################

plt.xlim((-0.5, 4.1))
plt.ylim((-459.5, -453))
##### para que sea larga la caja
#plt.figure(figsize=(10,6))
fig.set_size_inches(9, 4)

###############################################
### Graducion de ejes
###############################################
#plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
## Le pone string a los numeros del eje
plt.xticks(x1, x)
###############################################
### Notas
###############################################

#plt.title(r'Comparaci\'on de Bases y Funcionales')
#leg = ax1.legend(loc='lower left')
ax1.set_xlabel('Método y Base')
ax1.set_ylabel(r'$E$ (hartree)')


###############################################
### Imprimir
###############################################

ax1.plot(x1, y, marker='o')

plt.show()
fig.savefig('bases_f.pdf')
