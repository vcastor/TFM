#!/opt/homebrew/bin/python3
import numpy as np
#### Imprimir como antes
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
mpl.style.use('classic')
axis_font = {'size' : '20'}
from matplotlib import rcParams
#rcParams.update({'font.size' : 16})
#rcParams.update({'figure.autolayout' : True})

charge = []
Eadd   = []
Enet   = []
Eeff   = []
Kin    = []
DI     = []

archivo = open('chargee.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]), float(columns[5])
    charge.append(float(columns[0]))
    Eadd.append(float(columns[1]))
    Enet.append(float(columns[2]))
    Eeff.append(float(columns[3]))
    Kin.append(float(columns[4]))
    DI.append(float(columns[5]))
archivo.close()

x = np.array(charge)
y = np.array(Eadd)

#Eadd
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-', label=r'$E_{add}$ $r^2=0.96099$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='red')

#Enet
y  = np.array(Enet)
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

ax.plot(x, y_est, '-', label=r'$E_{net}$ $r^2=0.99145$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='blue')

#Eeff
y = np.array(Eeff)
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

ax.plot(x, y_est, '-', label=r'$E_{eff}$ $r^2=0.94330$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='green')

#Kin
y = np.array(Kin)
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

ax.plot(x, y_est, '-', label=r'$T$ $r^2=0.98476$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='m')

#DI
y = np.array(DI)
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

ax.plot(x, y_est, '-', label=r'$DI$ $r^2=0.99480$')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.1)
ax.plot(x, y, '.', color='black')

plt.title('Charge analysis', **axis_font)
plt.xlabel(r'charge (atomic units)', **axis_font)
plt.ylabel(r'atomic units', **axis_font)

#plt.ylim((-2.5, 5))
#plt.xlim((2, 10.5))

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.17,
                 box.width, box.height * 0.85])

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3)
#          fancybox=True, shadow=True, ncol=3)

plt.savefig('chargee.pdf')
#plt.show()
