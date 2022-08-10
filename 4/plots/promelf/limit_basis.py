#!/opt/homebrew/bin/python3
### Raw data
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import numpy as np
#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl 
mpl.style.use('classic')

###############################################
### Abrir data

x   = []
tz  = []
qz  = []
lim = []

archivo = open('limit_basis.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = str(columns[0]), float(columns[1]), float(columns[2]), float(columns[3])
    x.append(str(columns[0]))
    tz.append(float(columns[1]))
    qz.append(float(columns[2]))
    lim.append(float(columns[3]))
archivo.close()

# names to integer number
x1 = np.arange(len(x))
# but having the number for the plot
plt.xticks(x1, x)

plt.plot(x1,tz, color='blue', marker='o', label=r'pVTZ')
plt.plot(x1,qz, color='blue', marker='D', label=r'pVQZ')
plt.plot(x1,lim, color='blue', marker='*', label=r'limit')

###############################################
### Espacio de dibujo

plt.xlim((-0.5, 4.5))
#plt.ylim((-328.5,-328.0))

###############################################
### Notas

#plt.title('titulo')
plt.title('Basis dependency')
leg = plt.legend(loc='upper right')
plt.xlabel('Basis set')
plt.ylabel(r'E $\mathrm{(kJmol^{-1})}$')

###############################################
### Imprimir

plt.savefig('limit_corr.pdf')
#plt.show()

