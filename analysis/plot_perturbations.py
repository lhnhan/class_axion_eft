import sys
import numpy as np
import matplotlib.pyplot as plt

fname = "output/ax_params00_perturbations_k2_s.dat"
fname1 = "output/ax_params04_perturbations_k2_s.dat"


data = np.loadtxt(fname)
a = data[:,1]
delta_cdm = np.abs(data[:,15])
delta_ax = np.abs(data[:,17])

data1 = np.loadtxt(fname1)
a1 = data1[:,1]
delta1_ax = np.abs(data1[:,17])

fig, ax = plt.subplots()
ax.loglog(a, delta_cdm, color='blue')
ax.loglog(a, delta_ax, color='black')
ax.loglog(a1, delta1_ax, color='green')
# ax.set_xlim(1e-8, 1e-4)
# ax.set_ylim(1e6, 1e12)
plt.show()