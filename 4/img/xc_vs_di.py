import math
import pylab

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')
####

x = [-5.558, -5.107, -4.947, -4.752, -4.330, -4.130, -4.146, -4.080, -3.670, -3.395] #intercambio_correlacion
x1 = [-7, -2] #xlinear regression
y = [0.2180, 0.1990, 0.1986, 0.1832, 0.1727, 0.1731, 0.1688, 0.1623, 0.1492, 0.1394]#DI
z = [0.268, 0.091]#y linear regression
e1 = [0.391, 0.568, 0.187, 0.455, 0.283, 0.487, 0.411, 0.204, 0.232, 0.404]#xc_cr
e2 = [0.024, 0.018, 0.010, 0.009, 0.011, 0.009, 0.018, 0.006, 0.010, 0.016]#di

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
plt.xlim((-6.1, -2.9))
plt.ylim((0.11, 0.25))


#############################
########### Graducion de ejes
#############################
plt.xticks([-6, -5, -4, -3])
plt.yticks([0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.22, 0.24])


#############################
########### A dibujar
#############################
ax1.plot(x1,z, '-', c='red', label=r'Regresi\'on Lineal, $r^2 = 0.92$')
plt.errorbar(x,y, xerr=e1, yerr=e2, fmt='o', label=r'$V_{\mathrm{xc}}^{\, \prime}$ vs. DI')
#ax = sns.regplot(x=df[x], y=df[y], color="g", ci=95)

z_up=[0.283, 0.106]
z_low=[0.253, 0.076]

#ax1.plot(x1,z_up, '--', c='red', label=r'Confidence Intervals')
#ax1.plot(x1,z_low, '--', c='red')



#############################
###########Notas
#############################
#plt.title('Distance O-O')
leg = ax1.legend(loc='lower left')
ax1.set_xlabel(r'Intercambio-correlaci{\'o}n')
ax1.set_ylabel(r'DI')

#####################
plt.show()

fig.savefig('XC_vs_di.pdf')

