#!/opt/homebrew/bin/python3
import numpy as np
#### Imprimir como antes
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
mpl.style.use('classic')
axis_font = {'size' : '16'}
from matplotlib import rcParams
rcParams.update({'font.size' : 12})
#rcParams.update({'figure.autolayout' : True})

fig = plt.figure(figsize=(6,8))

x    = []
clin = []
xcin = []
cl1  = []
xc1  = []
t1   = []
v1   = []
di1  = []
cl2  = []
xc2  = []
t2   = []
v2   = []
di2  = []

archivo = open('homodromic.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8]), float(columns[9]), float(columns[10]), float(columns[11]), float(columns[12])
    x.append(float(columns[0]))
    clin.append(float(columns[1]))
    xcin.append(float(columns[2]))
    cl1.append(float(columns[3]))
    xc1.append(float(columns[4]))
    t1.append(float(columns[5]))
    v1.append(float(columns[6]))
    di1.append(float(columns[7]))
    cl2.append(float(columns[8]))
    xc2.append(float(columns[9]))
    t2.append(float(columns[10]))
    v2.append(float(columns[11]))
    di2.append(float(columns[12]))
archivo.close()

plt.plot(x, clin, color='blue', marker='.', label=r'Classic Interaction')
plt.plot(x, xcin, color='blue', marker='x', label=r'Exchange-Correlation Interaction')
plt.plot(x, cl1, color='red', marker='1', label=r'Classic Contr. H')
plt.plot(x, xc1, color='red', marker='2', label=r'Exchange-Correlation Contr. H')
plt.plot(x, t1,  color='red', marker='3', label=r'Kinetic Contr. H')
plt.plot(x, v1,  color='red', marker='4', label=r'Potential H')
plt.plot(x, cl2, color='green', marker='1', label=r'Classic Contr. e pair')
plt.plot(x, xc2, color='green', marker='2', label=r'Exchange-Correlation Contr.')
plt.plot(x, t2,  color='green', marker='3', label=r'Kinetic Contr. e pair')
plt.plot(x, v2,  color='green', marker='4', label=r'Potential e pair')


plt.xlabel(r'Homodromic Interactions', **axis_font)
plt.ylabel(r'Energy ($E_h$)', **axis_font)

plt.xlim((0, 13))
plt.ylim((-3, 5))

ax = plt.subplot(111)
#ax.legend(loc='upper left')#, bbox_to_anchor=(1, 0.5))
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 1.0, box.height * 0.6])
##ax.set_position([box.x0, box.y0, box.width * 1.0, box.height * 0.6])

# Put a legend to the right of the current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.8))
##ax.legend(loc='upper center', bbox_to_anchor=(0.5, 2.0))


plt.savefig('homodromic1.pdf')
#plt.show()
