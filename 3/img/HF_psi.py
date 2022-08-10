#!/opt/homebrew/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
import matplotlib.patches as mpatches
import math
import pylab
import matplotlib.ticker as ticker
mpl.style.use('classic')
axis_font = {'size':'16'}
#mpl.rcParams['errorbar.capsize'] = 3
from matplotlib import rcParams
rcParams.update({'font.size': 16})
rcParams.update({'figure.autolayout': True})

### Dibujaremos

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 4.5))
ax1 = fig.add_subplot(111)

for axis in [ax1.xaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

####################
x  = np.arange(0.0,2.5, 0.01)
#y1 = ((x+1.)**(3./2.)*(2.*x +1.)**(3./4.))/((0.5*((x+1.)**(0.5)+(2.*x+1.)**(0.5)))**3. *(0.5*(1.+(2.*x+1.)*(0.5)))**3.)
y1 = ((x + 1)**(3./2.))*((2*x + 1)**(3./4.))/(((0.5*(((x+1.)**0.5)+((2*x+1.)**0.5)))**3.)*((0.5*(1+((2*x+1)**0.5)))**3.))

#plt.plot(x,y1,'-',linewidth=1,color='b', label=r'hi')
plt.plot(x,y1,'-',linewidth=1,color='b', label=r'$(\Psi,\Psi_{HF})^2 = \frac{(\kappa +1)^{3/2}(2\kappa +1)^{3/4}}{[1/2(\sqrt{\kappa +1} + \sqrt{2\kappa +1})]^3[1/2(1+\sqrt{2\kappa +1})]^3}$')
#plt.hold(True)
#plt.axis('equal')
plt.xlabel('$k$', **axis_font)
plt.ylabel('Overlap', **axis_font)
plt.title('Overlap between $\Psi$ and $\Psi_{HF}$', **axis_font)
#plt.show()



### Espacio de dibujo
plt.xlim((0.0, 2.4))
plt.ylim((0., 1.))

### Graducion de ejes
plt.xticks([0.0, 0.5, 1.0, 1.5, 2.0])

### Notas
#plt.title('titulo')
#leg = ax1.legend(loc='lower left')

#plt.legend((r'$\Psi$'),
#plt.legend(r'$(\Psi,\Psi_{HF})^2 = \frac{(\kappa +1)^{3/2}(2\kappa +1)^{3/4}}{[1/2(\sqrt{\kappa +1} + \sqrt{2\kappa +1})]^3[1/2(1+\sqrt{2\kappa +1})]^3}$',
#       prop = {'size': 10}, loc='upper left')
plt.legend((r'$(\Psi,\Psi_{HF})^2 = \frac{(\kappa +1)^{3/2}(2\kappa +1)^{3/4}}{[1/2(\sqrt{\kappa +1} + \sqrt{2\kappa +1})]^3[1/2(1+\sqrt{2\kappa +1})]^3}$', r'$E=\frac{3}{2}\left[1+\sqrt{\mathstrut{2k+1}}\right]$'),
       prop = {'size': 20}, loc='upper right')
#       loc='upper right')


### Imprimir
#plt.show()
fig.savefig('HF_vs_psi.pdf')



