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

x   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
xc1 = []
xc2 = []

archivo = open('xc1_vs_xc2.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1])
    xc1.append(float(columns[0]))
    xc2.append(float(columns[1]))
archivo.close()

plt.plot(x,xc1, color='blue', marker='o', label=r'$\sum E_{xc}^{\mathrm{H}}$')
plt.plot(x,xc2, color='red', marker='o', label=r'$\sum E_{xc}^{\mathrm{e-pair}}$')

#xc1 = np.array(xc1)
#xc2 = np.array(xc2)

# fit a linear curve an estimate its y-values and their error.
#a, b = np.polyfit(xc1, xc2, deg=1)
#y_est = a * xc1 + b
#y_err = xc1.std() * np.sqrt(1/len(xc1) +
#                          (xc1 - xc1.mean())**2 / np.sum((xc1 - xc1.mean())**2))

#fig, ax = plt.subplots()
#ax.plot(xc1, y_est, '-')
#ax.fill_between(xc, y_est - y_err, y_est + y_err, alpha=0.1)
#ax.plot(xc1, xc2, '.', color='red', label='data points')

plt.title('Exchange-correlation Energy', **axis_font)
plt.xlabel(r'Dimer Cluster', **axis_font)
plt.ylabel(r'Energy ($\mathrm{E_h}$)', **axis_font)

plt.ylim((-3.2, 0.))
#plt.xlim((-470, -50))

plt.legend(loc='upper left')#, bbox_to_anchor=(1, 0.5))

plt.savefig('xc1_xc2.pdf')
#plt.show()
