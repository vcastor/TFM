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

x        = []
dft_tz   = []
dft_qz   = []
mp2_tz   = []
mp2_qz   = []

archivo = open('dimer_basis.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = str(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4])
    x.append(str(columns[0]))
    dft_tz.append(float(columns[1]))
    dft_qz.append(float(columns[2]))
    mp2_tz.append(float(columns[3]))
    mp2_qz.append(float(columns[4]))
archivo.close()

ax.ticklabel_format(useMathText=True)
ax.ticklabel_format(style = 'sci', axis='y', scilimits=(0,0))
ax.get_yaxis().get_major_formatter().set_useOffset(False)
# names to integer number
x1 = np.arange(len(x))
# but having the number for the plot
plt.xticks(x1, x)

plt.plot(x1,dft_tz, color='red', marker='.', label=r'DFT pVTZ')
plt.plot(x1,dft_qz, color='red', marker='^', label=r'DFT pVQZ')
plt.plot(x1,mp2_tz, color='blue', marker='.', label=r'MP2 pVTZ')
plt.plot(x1,mp2_qz, color='blue', marker='^', label=r'MP2 pVQZ')

plt.xlim((-0.5, 4.5))
#plt.ylim((-0.4,-0.12))

plt.title('Basis dependency', **axis_font)
leg = plt.legend(loc='center left')
plt.xlabel('Basis set', **axis_font)
plt.ylabel(r'$E$ $\mathrm{(kcalmol^{-1})}$', **axis_font)

#plt.show()
plt.savefig('dimer_basis.pdf')

