#!/opt/homebrew/bin/python3
import numpy as np
#### Imprimir como antes
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
from matplotlib.ticker import FormatStrFormatter
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%g'))
mpl.style.use('classic')
axis_font = {'size':'20'}
#mpl.rcParams['errorbar.capsize`] = 3
from matplotlib import rcParams
rcParams.update({'font.size' : 16})
rcParams.update({'figure.autolayout' : True})

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x1   = [1]
x2   = [1, 2, 3]
x3   = [1, 2, 3, 4]
dimer    = [2.9032]
edimer   = [0.0052]
trimer   = [2.7875, 2.7965, 2.7889]
etrimer  = [0.0023, 0.0056, 0.0024]
tetramer = [2.7450, 2.7423, 2.7423, 2.7424]
etetra   = [0.0101, 0.0102, 0.0055, 0.0101]

plt.errorbar(x1, dimer, yerr=edimer, marker='.', color='b', label=r'dimer')
plt.errorbar(x2, trimer, yerr=etrimer, marker='.', color='r', label=r'trimer')
plt.errorbar(x3, tetramer, yerr=etetra, marker='.', color='g', label=r'tetramer')

plt.xlim((0, 5))
plt.xticks(size=15)
plt.yticks(size=15)
#plt.xticks((1, 2, 3, 4, 5, 6))
#plt.ylim((-400,-140))

ax = plt.subplot(111)
ax.legend(loc='upper right')#, bbox_to_anchor=(1, 0.5))

plt.title(r'Distances between O atoms', **axis_font)
plt.xlabel(r'HB number', **axis_font)
plt.ylabel(r'distace $\mathrm{\AA}$', **axis_font)

plt.savefig('distances.pdf')
#plt.show()
