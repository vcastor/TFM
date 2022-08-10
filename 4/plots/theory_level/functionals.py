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
#mpl.rcParams['errorbar.capsize'] = 3
from matplotlib import rcParams
rcParams.update({'font.size': 14})
rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x       = []
x1      = [1,2,3,4,5,6]
wb97xd  = []
dsd     = []
m062d3  = []
m062x   = []
average = []
sigma   = []

archivo = open('functionals.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = int(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6])
    x.append(int(columns[0]))
    wb97xd.append(float(columns[1]))
    dsd.append(float(columns[2]))
    m062d3.append(float(columns[3]))
    m062x.append(float(columns[4]))
    average.append(float(columns[5]))
    sigma.append(float(columns[6]))
archivo.close()

for i in range(len(x)):
    wb97xd[i] = wb97xd[i]*627.5/x[i]
    dsd[i] = dsd[i]*627.5/x[i]
    m062d3[i] = m062d3[i]*627.5/x[i]
    m062x[i] = m062x[i]*627.5/x[i]
    average[i] = average[i]*627.5/x[i]
    sigma[i] = sigma[i]*627.5/x[i]

plt.plot(x1, wb97xd, marker='.', color='blue', label=r'xB97XD')
plt.plot(x1, dsd, marker='.', color='red', label=r'DSD')
plt.plot(x1, m062d3, marker='.', color='green', label=r'M06D3')
plt.plot(x1, m062x, marker='.', color='orange', label=r'M06-2X')
plt.errorbar(x1, average, yerr=sigma, marker='.', color='m', label=r'average')

plt.xlim((0.5, 6.5))
plt.ylim((-48035, -47900))
ax.ticklabel_format(useMathText=True)
ax.ticklabel_format(style = 'sci', axis='y', scilimits=(0,0))
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.xticks(x1, ["monomer","dimer", "trimer", "tetramer", "pentamer\nc", "pentamer\np"], size=15)
plt.yticks(size=15)

ax = plt.subplot(111)
ax.legend(loc='lower left')

plt.title(r'Energy at different theory levels', **axis_font)
plt.xlabel(r'Water Cluster', **axis_font)
plt.ylabel(r'$E/n$ $(\mathrm{kcal/mol})$', **axis_font)

#plt.show()
plt.savefig('functionals.pdf')
