#!/usr/bin/python3
import argparse
import sqlite3
import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

parser = argparse.ArgumentParser(description='Query a synthetic spectra database.')
parser.add_argument('-d', required=True, type=str,
    metavar='<str>', help='Path to SQLite Database (%(type)s)')
parser.add_argument('-t', required=True, type=str,
    metavar='<str>', help='Name of table to insert into (%(type)s)')
    
arg = parser.parse_args()

conn = sqlite3.connect(arg.d)
c = conn.cursor()

c.execute('SELECT * from {tn}'.format(tn=arg.t))
rows = c.fetchone()
print(rows[2])

for i, r in enumerate(rows):
	print(i)

img = np.frombuffer(rows[2], dtype = np.uint8).reshape((300,300))
print(img)
plt.imshow(img, cmap="gray", aspect='auto')
plt.axis('off')
plt.show()

conn.commit()
conn.close()
