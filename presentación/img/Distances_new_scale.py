import math
import pylab

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

#### Imprimir como antes
# import matplotlib.style
# import matplotlib as mpl
# mpl.style.use('classic')
####


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [2.849, 2.799, 2.760, 2.776, 2.745, 2.757, 2.723, 2.715, 2.699, 2.646]
z = [2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76]
e = [0.046, 0.034, 0.040, 0.050, 0.030, 0.025, 0.013, 0.020, 0.034, 0.032]

#############################
########### Dibujo de grafica
#############################
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure()
ax1 = fig.add_subplot(111)

for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))


#############################
########### Espacio de Dibujo
#############################
plt.xlim((0.5, 10.5))
plt.ylim((2.55, 2.95))


#############################
########### Graducion de ejes
#############################
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#plt.yticks([])


#############################
########### A dibujar
#############################
ax1.plot(x1,z, '-', c='red', label=r'Hielo $\mathrm{I_{h}}$')
plt.errorbar(x,y, yerr=e, c='blue', marker='o', label=r'Distancia O-O')

#############################
###########Notas
#############################
#plt.title('Distance O-O')
leg = ax1.legend(loc='lower left')
ax1.set_xlabel('Tipo de EH')
ax1.set_ylabel(r'Distancia (\AA)')

#####################
plt.show()

fig.savefig('Distances_O-O_new_scale.pdf')
