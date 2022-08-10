##############################################
### Raw data

import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
#### Imprimir como antes
import matplotlib.style
import matplotlib as mpl 
mpl.style.use('classic')

###############################################
### Abrir data

x     = []
hfdzp = []
hftzp = []
hfqzp = []
ccdzp = []
cctzp = []
cidzp = []
citzp = []
ciqzp = []

archivo = open('vs_dt.dat', 'r')
for line in archivo:
    line = line.strip()
    columns = line.split()
    source = float(columns[0]), float(columns[1]), float(columns[2]), float(columns[3]), float(columns[4]), float(columns[5]), float(columns[6]), float(columns[7]), float(columns[8])
    x.append(float(columns[0]))
    hfdzp.append(float(columns[1]))
    hftzp.append(float(columns[2]))
    hfqzp.append(float(columns[3]))
    ccdzp.append(float(columns[4]))
    cctzp.append(float(columns[5]))
    cidzp.append(float(columns[6]))
    citzp.append(float(columns[7]))
    ciqzp.append(float(columns[8]))
archivo.close()

plt.plot(x,hfdzp, color='red', marker='.', label=r'HF Sapporo-DZP')
plt.plot(x,hftzp, color='red', marker='1', label=r'HF Sapporo-TZP')
plt.plot(x,hfqzp, color='red', marker='2', label=r'HF Sapporo-QZP')
plt.plot(x,ccdzp, color='green', marker='.', label=r'CC-SD Sapporo-DZP')
plt.plot(x,cctzp, color='green', marker='1', label=r'CC-SD Sapporo-TZP')
plt.plot(x,cidzp, color='blue', marker='.', label=r'CI-SD Sapporo-DZP')
plt.plot(x,citzp, color='blue', marker='1', label=r'CI-SD Sapporo-TZP')
plt.plot(x,ciqzp, color='blue', marker='2', label=r'CI-SD Sapporo-QZP')

###############################################
### Espacio de dibujo

plt.xlim((1.0, 6.0))
plt.ylim((-328.5,-328.0))

###############################################
### Notas

#plt.title('titulo')
leg = plt.legend(loc='center right')
plt.xlabel('Distance $\mathrm{(\AA)}$')
plt.ylabel(r'E $\mathrm{(E_h)}$')

#plt.tight_layout(rect=[0,0,0.75,1])
#leg = plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
# Shrink current axis by 20%
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

###############################################
### Imprimir

plt.savefig('vs_dt_hfcicc_q_.pdf')
plt.show()

