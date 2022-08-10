##############################################
### energy wfn promelf dimer
###############################################

import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker

### Dibujaremos

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()
ax1 = fig.add_subplot(111)

for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

### Abrir data

x    = []
wfn  = []
wfne = []
pro  = []
proe = []


archivo = open('e_wfn_promelf_dimer.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = int(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4])
    x.append(int(columns[0]))
    pro.append(float(columns[1]))
    proe.append(float(columns[2]))
    wfn.append(float(columns[3]))
    wfne.append(float(columns[4]))
archivo.close()

plt.errorbar(x, wfn, yerr=wfne, color='red', marker='o')
plt.errorbar(x, pro, yerr=proe, color='blue', marker='o')

### Espacio de dibujo

#plt.xlim((0.5, 10.5))
#plt.ylim((-11.0, 0.0))

### Graducion de ejes
#plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

### Notas

#plt.title('titulo')
#leg = ax1.legend(loc='lower left')
#ax1.set_xlabel('Tipo EH')
#ax1.set_ylabel(r'$E$ $(\mathrm{kcalmol^{-1}})$')


### Imprimir

plt.show()
#fig.savefig('Cl_xc.pdf')

