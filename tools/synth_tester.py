#!/usr/bin/python3
import sys
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
#parser.add_argument('-t', required=True, type=str,
#metavar='<str>', help='Name of table to insert into (%(type)s)')
parser.add_argument('-p', required=True, type=int,
	metavar='value', help='Number of points for the peak generator')
parser.add_argument('-s', required=True, type=str,
	metavar='schema', help='Path to schema')
parser.add_argument('-m', required=False, type=str,
	metavar='<str>', help='Mode for placing peaks in spectrum')

arg = parser.parse_args()

conn = sqlite3.connect(arg.d)
#PRAGMA
#conn.execute("PRAGMA foreign_keys")
c = conn.cursor()
#fixed dropping table
try:
	c.execute(f"DROP TABLE data")
	c.execute(f"DROP TABLE img_specs")
	c.execute(f"DROP TABLE plot_specs")
	with open(arg.s) as fp:
		c.executescript(fp.read())
except:
	with open(arg.s) as fp:
		c.executescript(fp.read())

sql = ''.join((f'INSERT OR IGNORE INTO data (points, np_plot, center_coords, ',
			   'plot_pixels, centers_pixels, todays_date, img_specs_id, plot_specs_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'))
print(sql)
xyz, mm, vv = gen.peak_generator(arg.p, mode="uniform")
img, peaks = gen.spectra_generator(xyz, mm)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(xyz[:,:,0],xyz[:,:,1],xyz[:,:,2], 100, cmap="gray_r")
plt.axis('off')
plt.show()

def img_specs_inserter(cursor):
	img_sql = ((f'INSERT INTO img_specs (figsize, dpi) VALUES (?, ?)')) ###function
	inserter_img = ['3in', '100']
	cursor.execute(img_sql, inserter_img)
#	return conn

def img_specs_query(cursor):
	img_spec_q = cursor.execute(f"SELECT id FROM img_specs WHERE figsize = '3in' AND dpi = '100'") ###function
	img_specs_id = cursor.fetchone()[0]
	return img_specs_id
#print(img_specs_id)

plot_sql = ''.join((f'INSERT INTO plot_specs (density, lower_limit, upper_limit, mode, ',
				'variance) VALUES (?, ?, ?, ?, ?)'))
inserter_plot = [1000.0, 0.0, 10.0, 'default', 1.0]
c.execute(plot_sql, inserter_plot)

plot_specs_q = c.execute(f"SELECT id FROM plot_specs WHERE density = 1000.0 AND lower_limit = 0.0 AND upper_limit = 10.0 AND mode = 'default' AND variance = 1.0 ")
plot_specs_id = c.fetchone()[0]

img_specs_inserter(c)


inserter = [arg.p, xyz.tobytes(), mm.tobytes(), img.tobytes(), peaks.tobytes(), '01/01/01', img_specs_query(c), plot_specs_id]

c.execute(sql, inserter)
#executing the inserter to insert information into the data,
#So we need sql (the command that inserts into the table "data", and we also need the inserter itself

#executor for the img_specs

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
