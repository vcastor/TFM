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

x        = []
xcint    = []
errxcint = []
cou      = []
errcou   = []
xcastor  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
castor20 = [-5.804, -6.165, -6.410, -6.947, -6.927, -7.340, -7.829, -8.570, -8.692, -9.551]
ecastor  = [0.912, 0.458, 1.088, 0.524, 0.575, 0.633, 0.035, 0.329, 0.660, 0.551]

archivo = open('types.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2])
    x.append(float(columns[0]))
    xcint.append(float(columns[1]))
    errxcint.append(float(columns[2]))
archivo.close()

for i in range(len(xcint)):
    xcint[i] = xcint[i]*627.5
    errxcint[i] = errxcint[i]*627.5

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.errorbar(x, xcint, yerr=errxcint, marker='o', color='r', label=r'$E_{\mathrm{xc}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}}$ this work') 
#plt.errorbar(xcastor, castor20, yerr=ecastor, marker='o', color='b', label=r'$E_{\mathrm{xc}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}}$ this work')
plt.errorbar(xcastor, castor20, yerr=ecastor, marker='o', color='b', label=r'$E_{\mathrm{xc}}^{\mathrm{H_2O}\cdots\mathrm{H_2O}^{ \, \prime}}$ in 12') 
#plt.errorbar(x, cou,   yerr=errcou,  marker='o', color='r', label=r'Cou')

plt.ylabel(r'Energy ($\mathrm{kcal/mol}$)', **axis_font)
plt.xlabel(r'Type of Hydrogen Bond', **axis_font)

plt.xlim((0.5, 11.5))
#plt.ylim((-76.5, -76.0))
plt.xticks([1,2,3,4,5,6,7,8,9,10])

plt.title('Energy in differents types of HB', **axis_font)
ax.legend(loc='lower left')

plt.savefig('types.pdf')
#plt.show()
