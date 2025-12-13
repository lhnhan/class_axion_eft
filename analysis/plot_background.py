import numpy as np
import matplotlib.pyplot as plt

fname = "output/ax_params00_background.dat"

data = np.loadtxt(fname)
a = 1/(data[:,0]+1)
rho_cdm = data[:,10]
rho_a = data[:,14]

# fname = "output/ax_params04_background.dat"

# data1 = np.loadtxt(fname)
# a1 = 1/(data1[:,0]+1)
# rho1_a = data1[:,14]

fig, ax = plt.subplots()
ax.loglog(a, rho_cdm, color='blue')
ax.loglog(a, rho_a, color='black')
# ax.loglog(a, rho1_a, color='orange')
ax.set_xlim(1e-8, 1e-4)
ax.set_ylim(1e6, 1e12)
plt.show()