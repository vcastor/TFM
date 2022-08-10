#!/opt/homebrew/bin/python3
import numpy as np
from scipy.interpolate import interp1d
#### Imprimir como antes
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
mpl.style.use('classic')
axis_font = {'size' : '20'}
from matplotlib import rcParams
rcParams.update({'font.size' : 16})
rcParams.update({'figure.autolayout' : True})

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x  = []
xc = []

archivo = open('xc_int.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1])
    x.append(float(columns[0]))
    xc.append(float(columns[1]))
archivo.close()

for i in range(len(x)):
        xc[i] = xc[i]*627.5

xnew = np.linspace(1, 15, num=15, endpoint=True)
f_cubic = interp1d(xnew, xc, kind=3)

plt.plot(x, xc, 'o', color='blue', label=r'$\sum E_{\mathrm{xc}}^{\mathrm{int}}$')
plt.plot(xnew, f_cubic(xnew), '-')

plt.title(r'Sum of exchange-correlation Energy', **axis_font)
plt.xlabel(r'Dimer Cluster', **axis_font)
plt.ylabel(r'$E$ $(\mathrm{kcal/mol})$', **axis_font)

plt.ticklabel_format(style = 'plain')
ax.get_yaxis().get_major_formatter().set_useOffset(False)

plt.xlim((0, 17))
#plt.ylim((-0.015, -0.005))
ax.ticklabel_format(useMathText=True)
ax.ticklabel_format(style = 'sci', axis='y', scilimits=(0,0))
ax.get_yaxis().get_major_formatter().set_useOffset(False)

ax = plt.subplot(111)
ax.legend(loc='upper left')#, bbox_to_anchor=(1, 0.5))

plt.savefig('xc_int.pdf')
#plt.show()
