#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Import data from csv using pandas and convert to numpy array
directory = os.path.dirname(__file__)
filename = 'langmuir_Ne_80v_3mbar.csv'
data = pd.read_csv(os.path.join(directory, filename))

voltage = data['Voltage [V]'].values
current = data['Current [?A]'].values

# Plot all data
fig, ax = plt.subplots(2, sharex=True)
ax[0].plot(voltage)
ax[1].plot(current)
ax[0].set_title(filename)
ax[0].set_ylabel('Voltage [V]')
ax[1].set_ylabel('Current [mA]')
ax[1].set_xlabel('Time [a.u.]')

# Choose data
begin = 400
end = 433
chosen_voltage = voltage[begin:end]
chosen_current = current[begin:end]

# Fit data
def f(v, isat, vf, te):
    return isat * (1 - np.exp((v - vf) / te))
popt, pcov = curve_fit(f, chosen_voltage, chosen_current)
perr = np.sqrt(np.diag(pcov))
fitted_current = f(chosen_voltage, *popt)
rmse = np.sqrt(
    np.sum((chosen_current - fitted_current) ** 2) / (end - begin + 1))

# Plot chosen data and fit results
pnames = ['Isat', 'Vf', 'Te']
punits = ['mA', 'V', 'eV']
results = ''
for name, value, error, units in zip(pnames, popt, perr, punits):
    results += '{} = {:.2f}$\pm${:.2f} {}\n'.format(name, value, error, units)
results += 'RMSE = {:.2f} {}'.format(rmse, punits[0])
fig2, ax2 = plt.subplots(1)
ax2.plot(chosen_voltage, chosen_current, '.', label='data')
ax2.plot(
    chosen_voltage, fitted_current, 
    label='fit: ${}(1-e^{{(V - {}) / {}}})$'.format(*pnames))
ax2.legend()
ax2.annotate(results, xy=(0.02, 0.55), xycoords='axes fraction')
ax2.set_title("{}, range = {}:{}".format(filename, begin, end))
ax2.set_xlabel('Voltage [V]')
ax2.set_ylabel('Current [mA]')
plt.show(block=True)
