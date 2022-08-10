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

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

wfn  = []
xc   = []

archivo = open('wfn_xc.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1])
    wfn.append(float(columns[0]))
    xc.append(float(columns[1]))
archivo.close()

x = np.array(wfn)
y = np.array(xc)

# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-', label=r'$y=1.3335x+203.8$, $r^2=0.84$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='red', label='data points')

plt.title(r'Exchange-correlation vs Electronic Energy')
plt.xlabel(r'Total Electronic Energy', **axis_font)
plt.ylabel(r'Exchange-correlation Energy', **axis_font)

plt.ticklabel_format(useMathText=True)
plt.ticklabel_format(style = 'sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style = 'sci', axis='y', scilimits=(0,0))
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_xaxis().get_major_formatter().set_useOffset(False)
#pyplot.locator_params(axis='x', nbins=7)
ax.xaxis.set_major_locator(plt.MaxNLocator(7))

plt.xlim((-152.869, -152.862))
plt.ylim((-0.015, -0.004))

ax = plt.subplot(111)
ax.legend(loc='upper left')#, bbox_to_anchor=(1, 0.5))

plt.savefig('wfn_xc.pdf')
#plt.show()
