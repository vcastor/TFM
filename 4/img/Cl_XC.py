##############################################
### Aportacion Clasica, Intercambio/Correlacion
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
### Abrir data
###############################################

#Read the first file
x  = []
ycl = []
yxc= []
ecl = []
exc = []
y = []
e = []

archivo = open('Cl_XC.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = int(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]) 
    x.append(int(columns[0]))
    y.append(float(columns[1]))
    e.append(float(columns[2]))
    ycl.append(float(columns[3]))
    ecl.append(float(columns[4]))
    yxc.append(float(columns[5]))
    exc.append(float(columns[6]))
archivo.close()


#errorbar(x, ycl, ecl)


plt.errorbar(x,ycl, yerr=ecl, color='red', marker='o', label=r'$V_{\mathrm{cl}}^{\, \prime}$')

plt.errorbar(x,yxc, yerr=exc, color='blue', marker='o', label=r'$V_{\mathrm{xc}}^{\, \prime}$')

plt.errorbar(x,y, yerr=e, color='green', marker='o',
		label=r'$E_{\mathrm{int}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}^{\, \prime}}$')



###############################################
### Espacio de dibujo
###############################################

plt.xlim((0.5, 10.5))
plt.ylim((-11.0, 0.0))

###############################################
### Graducion de ejes
###############################################
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

###############################################
### Notas
###############################################

#plt.title('titulo')
leg = ax1.legend(loc='lower left')
ax1.set_xlabel('Tipo EH')
ax1.set_ylabel(r'$E$ $(\mathrm{kcalmol^{-1}})$')


###############################################
### Imprimir
###############################################

plt.show()
fig.savefig('Cl_XC.pdf')





















