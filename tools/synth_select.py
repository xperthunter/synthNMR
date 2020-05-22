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
#print(rows[2])

for i, r in enumerate(rows):
	print(i)

img = np.frombuffer(rows[4], dtype = np.uint8).reshape((300,300))
xyz = np.frombuffer(rows[2], dtype = np.float64).reshape((1000,1000,3))
mm = np.frombuffer(rows[3], dtype = np.float64).reshape((rows[1],2))
#print(mm)
#print(xyz[0,0,0], xyz[-1,-1,0])
#print(xyz[0,0,1], xyz[-1,-1,1])
#print(xyz[0,0,2], xyz[-1,-1,2])
#print(img)
plt.imshow(img, cmap="gray", aspect='auto')
plt.axis('off')
plt.show()


c.execute(f"select count(*) from {arg.t}")
results = c.fetchone()
#print(results)
#print(rows[1])

conn.commit()
conn.close()
