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

xc = []
di = []

archivo = open('di_xc_e.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1])
    xc.append(float(columns[0]))
    di.append(float(columns[1]))
archivo.close()

xc = np.array(xc)
di = np.array(di)

# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(xc, di, deg=1)
y_est = a * xc + b
y_err = xc.std() * np.sqrt(1/len(xc) +
                          (xc - xc.mean())**2 / np.sum((xc - xc.mean())**2))

fig, ax = plt.subplots()
ax.plot(xc, y_est, '-', label=r'$y=-1.975x-0.248$, $r^2 = 0.9923$')
ax.fill_between(xc, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(xc, di, '.', color='red', label='data points')

plt.xlabel(r'Exchagne-correlation Energy', **axis_font)
plt.ylabel(r'Delocalization Index', **axis_font)

plt.title('DI vs XC electron pair', **axis_font)
#plt.ylim((-470, -50))
#plt.xlim((-470, -50))

ax.legend(loc='lower left')#, bbox_to_anchor=(1, 0.5))

plt.savefig('xc_di_e.pdf')
#plt.show()
