#!/opt/homebrew/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl 
mpl.style.use('classic')
axis_font = {'size':'20'}
from matplotlib import rcParams
rcParams.update({'font.size' : 16})
rcParams.update({'figure.autolayout' : True})

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

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
plt.ylim((-1600,-1320))
plt.xticks(size=15)
plt.yticks(size=15)

###############################################
### Notas

#plt.title('titulo')
plt.title('Basis dependency', **axis_font)
leg = plt.legend(loc='upper right')
plt.xlabel('Basis set', **axis_font)
plt.ylabel(r'$E$ $\mathrm{(kcalmol^{-1})}$', **axis_font)

###############################################
### Imprimir

plt.savefig('limit_basis.pdf')
#plt.show()

