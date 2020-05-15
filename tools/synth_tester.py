#!/usr/bin/python3
import argparse
import sqlite3
import numpy as np
import NMR_spectrum_generator_v2 as gen
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

parser = argparse.ArgumentParser(description='Make a synthetic spectra database.')
parser.add_argument('-d', required=True, type=str,
    metavar='<str>', help='Path to SQLite Database (%(type)s)')
parser.add_argument('-t', required=True, type=str,
    metavar='<str>', help='Name of table to insert into (%(type)s)')
parser.add_argument('-p', required=True, type=int,
	metavar='value', help='Number of points for the peak generator')
    
arg = parser.parse_args()

conn = sqlite3.connect(arg.d)
c = conn.cursor()

sql = 'INSERT OR IGNORE INTO {tn} (np_array, pixel_plot, pixel_peak) VALUES(?, ?, ?)'.format(tn = arg.t)
xyz, mm, vv = gen.peak_generator(arg.p, mode="uniform")
img, peaks = gen.spectra_generator(xyz, mm)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(xyz[:,:,0],xyz[:,:,1],xyz[:,:,2], 100, cmap="gray_r")
plt.axis('off')
plt.show()

inserter = [xyz.tobytes(), img.tobytes(), peaks.tobytes(),]

c.execute(sql, inserter)

conn.commit()
conn.close()
print(img.shape)
#plt.axes.get_xaxis().set_visible(False)
#plt.axes.get_yaxis().set_visible(False)
plt.imshow(img, cmap="gray", aspect='auto')
plt.axis('off')
plt.show()
#plt.imshow(img)
#plt.show()
#plt.imshow(peaks)
#plt.show()
