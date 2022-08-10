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

x = []
y = []

archivo = open('rl_v1_v2.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1])
    x.append(float(columns[0]))
    y.append(float(columns[1]))
archivo.close()

x = np.array(x)
y = np.array(y)

# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-', label=r'$y=1.5709+0.0060$, $r^2=0.9994$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='red', label='data points')

plt.title('Potential Energy Contributin', **axis_font)
plt.xlabel(r'H Energy contribution ($\mathrm{E_h}$)', **axis_font)
plt.ylabel(r'e pair Energy contribution ($\mathrm{E_h}$)', **axis_font)

plt.ylim((-13.5,-1))
plt.xlim((-7.8,-1.2))

ax.legend(loc='upper left')#, bbox_to_anchor=(1, 0.5))

plt.savefig('rl_v1_v2.pdf')
#plt.show()
