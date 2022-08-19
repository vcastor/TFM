#!/opt/homebrew/bin/python3#
#from pylab import *
#import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import math
import pylab
import matplotlib.ticker as ticker
mpl.style.use('classic')
axis_font = {'size':'20'}
#mpl.rcParams['errorbar.capsize'] = 3
from matplotlib import rcParams
rcParams.update({'font.size': 16})
rcParams.update({'figure.autolayout': True})

###############################################
### Dibujaremos
###############################################

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()
ax1 = fig.add_subplot(111)

for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))


####################
x = np.arange(0.0,4.0, 0.01)
y1 = 3*(x+1)**(1./2.)
y2 = (3./2.)*(1+((2*x+1)**(1./2.)))
####################

plt.plot(x,y1,'-',linewidth=1,color='b', label=r'3\sqrt{\mathstrut{1+k}}')
#plt.hold(True)
plt.plot(x,y2,'-',linewidth=1,color='g', label=r'\frac{3}{2}[1+\sqrt{\mathstrut{2k+1}}]')
#plt.axis('equal')
plt.xlabel('$k$', **axis_font)
plt.ylabel('$E$', **axis_font)
plt.title('$E_{HF}$ vs $E_{exact}$', **axis_font)
#plt.show()



###############################################
### Espacio de dibujo
###############################################

plt.xlim((0.0, 2.0))
plt.ylim((3.0, 5.3))

###############################################
### Graducion de ejes
###############################################
plt.xticks([0.0, 0.5, 1.0, 1.5, 2.0])

###############################################
### Notas
###############################################

#plt.title('titulo')
#leg = ax1.legend(loc='lower left')

plt.legend((r'$E_{HF}=3\sqrt{\mathstrut{1+k}}$', r'$E=\frac{3}{2}\left[1+\sqrt{\mathstrut{2k+1}}\right]$'),
       prop = {'size': 20}, loc='upper left')

###############################################
### Imprimir
###############################################

#plt.show()
#fig.savefig('HF_vs_excat.pdf')
