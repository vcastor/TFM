#!/opt/homebrew/bin/python3
import numpy as np
#### Imprimir como antes
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
mpl.style.use('classic')
axis_font = {'size' : '20'}
from matplotlib import rcParams
rcParams.update({'font.size' : 14})
rcParams.update({'figure.autolayout' : True})

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x        = []
promelf  = []
wfn      = []

archivo = open('dimer_energywfn.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2])
    x.append(float(columns[0]))
    promelf.append(float(columns[1]))
    wfn.append(float(columns[2]))
archivo.close()

plt.plot(x, promelf, color='red',  marker='.', label=r'\sc{Promelf}')
plt.plot(x, wfn,     color='blue', marker='.', label=r'\sc{Gaussian16}')

plt.title(r'Energy fluctuations in dimer clusters', **axis_font)
plt.xlabel(r'Dimer Cluster', **axis_font)
plt.ylabel(r'$E-\mathrm{Max}(E)$ ($\mathrm{kcal/mol}$)', **axis_font)

plt.xlim((0, 17))
plt.ylim((-40, 8.0))
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

ax = plt.subplot(111)
ax.legend(loc='upper left')#, bbox_to_anchor=(1, 0.5))

plt.savefig('dimer_energywfn.pdf')
#plt.show()
