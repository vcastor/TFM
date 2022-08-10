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
rcParams.update({'font.size' : 14})
rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x    = []
x1   = [1,2,3,4,5]
mp2  = []
dft  = []
pro  = []

archivo = open('mp2dftpromelf.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = int(columns[0]), float(columns[1]), float(columns[2]), float(columns[3])
    x.append(int(columns[0]))
    mp2.append(float(columns[1]))
    dft.append(float(columns[2]))
    pro.append(float(columns[3]))
archivo.close()

for i in range(len(x)):
    mp2[i] = mp2[i]*627.5/x[i]
    dft[i] = dft[i]*627.5/x[i]
    pro[i] = pro[i]*627.5/x[i]

plt.plot(x1, mp2, marker='.', color='blue', label=r'MP2')
plt.plot(x1, dft, marker='.', color='red', label=r'DFT (M06-2X)')
plt.plot(x1, pro, marker='.', color='green', label=r'\sc{Promelf}')

plt.xlim((0.5, 5.5))
plt.ylim((-48200,-46400))
plt.ticklabel_format(useMathText=True)
plt.ticklabel_format(style = 'sci', axis='y', scilimits=(0,0))
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.xticks(x1, ["dimer", "trimer", "tetramer", "pentamer\nc", "pentamer\np"], size=15)
plt.yticks(size=15)

ax = plt.subplot(111)
ax.legend(loc='upper right')#, bbox_to_anchor=(1, 0.5))

plt.title(r'Energy at different theory levels', **axis_font)
plt.xlabel(r'Water Cluster', **axis_font)
plt.ylabel(r'$E/n$ $(\mathrm{kcal/mol})$', **axis_font)

#plt.show()
plt.savefig('mp2dftpromelf.pdf')
