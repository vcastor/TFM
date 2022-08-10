#!/opt/homebrew/bin/python3
import numpy as np
#### Imprimir como antes
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
mpl.style.use('classic')
axis_font = {'size' : '20'}
from matplotlib import rcParams
rcParams.update({'font.size' : 16})
rcParams.update({'figure.autolayout' : True})

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x        = []
promelf  = []
promelfe = []
wfn      = []
wfne     = []
x1       = [-1, 7]
h2op     = [-76.09004764, -76.09004764]
h2ow     = [-76.430106737419, -76.430106737419]

archivo = open('energy_devided.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4])
    x.append(float(columns[0]))
    promelf.append(float(columns[1]))
    wfn.append(float(columns[2]))
    promelfe.append(float(columns[3]))
    wfne.append(float(columns[4]))
archivo.close()

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.errorbar(x, promelf, yerr=promelfe, fmt='.', color='r', label=r'\sc{Promelf}')
plt.errorbar(x, wfn,     yerr=wfne,     fmt='.', color='b', label=r'{\sc{Gaussian16}}')
matplotlib.pyplot.plot(x1, h2op, '-', color='r')
matplotlib.pyplot.plot(x1, h2ow, '-', color='b')

plt.xlabel(r'Water molecules per cluster', **axis_font)
plt.ylabel(r'Energy per water molecule ($\mathrm{E_h}$)', **axis_font)

plt.xlim((0.5, 6.5))
plt.ylim((-76.5, -76.0))
plt.xticks(np.arange(1,7))
plt.yticks(np.arange(-76.5,-75.9,0.1), ["-76.5", "-76.4", "-76.3", "-76.2", "-76.1", "-76.0" ])
#plt.ax.set_yticklabels(np.arange(-76.5,-76.0,0.1))

plt.title(r'Energy in different clusters', **axis_font)
ax.legend(loc='center left')

plt.savefig('devided.pdf')
#plt.show()
