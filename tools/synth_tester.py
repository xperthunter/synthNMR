#!/usr/bin/python3
import datetime
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
#parser.add_argument('-m', required=False, type=str,
	#metavar='<str>', help='Mode for placing peaks in spectrum')

arg = parser.parse_args()
#print(datetime.date.today())
conn = sqlite3.connect(arg.d)

c = conn.cursor()
#fixed dropping table
try:
	c.execute("DROP TABLE data")
	c.execute("DROP TABLE img_specs")
	c.execute("DROP TABLE plot_specs")
	c.execute("DROP TABLE user_info")
	with open(arg.s) as fp:
		c.executescript(fp.read())
except:
	with open(arg.s) as fp:
		c.executescript(fp.read())

sql = ''.join(('INSERT OR IGNORE INTO data (points, np_plot, center_coords, ',
			   'plot_pixels, centers_pixels, todays_date, img_specs_id, plot_specs_id,',
			   ' user_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'))
print(sql)
xyz, mm, vv = gen.peak_generator(arg.p, mode="uniform")
img, peaks = gen.spectra_generator(xyz, mm)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(xyz[:,:,0],xyz[:,:,1],xyz[:,:,2], 100, cmap="gray_r")
plt.axis('off')
plt.show()

#img_specs table
def img_specs_inserter(cursor, inserter_img1):
	img_sql = ((f'INSERT INTO img_specs (figsize, dpi) VALUES (?, ?)')) ###function
	#inserter_img = ['3in', '100']
	cursor.execute(img_sql, inserter_img1)
#connecting to the table data; foreign key = img_specs_id
def img_specs_query(cursor, query_img): ###arguments
	img_spec_q = cursor.execute(''.join((f"SELECT id FROM img_specs WHERE figsize = '{query_img[0]}'",
		    							 f" AND dpi = '{query_img[1]}'")))
	img_specs_id = cursor.fetchone()[0]
	args = locals().copy()
	return img_specs_id, args
#print(img_specs_id)

#plot_specs table
def plot_specs_inserter(cursor, inserter_plot):
	plot_sql = ''.join((f'INSERT INTO plot_specs (density, lower_limit, upper_limit, mode, ',
					'variance) VALUES (?, ?, ?, ?, ?)'))
	#inserter_plot = [1000.0, 0.0, 10.0, 'default', 1.0]
	cursor.execute(plot_sql, inserter_plot)

def plot_specs_query(cursor, query_plot):
	plot_specs_q = cursor.execute(''.join((f"SELECT id FROM plot_specs WHERE density = '{query_plot[0]}' AND",
										   f" lower_limit = '{query_plot[1]}' AND upper_limit = '{query_plot[2]}'",
										   f" AND mode = '{query_plot[3]}' AND variance = '{query_plot[4]}'")))
	plot_specs_id = cursor.fetchone()[0]
	args = locals().copy()
	return plot_specs_id, args

#user_info table
def user_info_inserter(cursor, inserter_user):
	user_sql = ((f'INSERT INTO user_info (first_name, last_name, email) VALUES (?, ?, ?)'))
	#inserter_user = ['Stephani', 'Keefe', 'skeefe@ucdavis.edu']
	cursor.execute(user_sql, inserter_user)

def user_info_query(cursor, query_user):
	user_specs_q = cursor.execute(''.join((f"SELECT id FROM user_info WHERE first_name = '{query_user[0]}'",
										   f" AND last_name = '{query_user[1]}' AND email = '{query_user[2]}'")))
	user_id = cursor.fetchone()[0]
	args = locals().copy()
	return user_id, args


img_specs_inserter(c, ['3in', '100'])
x,a = img_specs_query(c,['3in', '100'])

plot_specs_inserter(c, [1000.0, 0.0, 10.0, 'default', 1.0])
a,b = plot_specs_query(c,[1000.0, 0.0, 10.0, 'default', 1.0])

user_info_inserter(c, ['Stephani', 'Keefe', 'skeefe@ucdavis.edu'])
d,e = user_info_query(c,['Stephani', 'Keefe', 'skeefe@ucdavis.edu'])

#print(a)
#sys.exit()

inserter = [arg.p,
			xyz.tobytes(),
			mm.tobytes(),
			img.tobytes(),
			peaks.tobytes(),
			datetime.date.today(),
			img_specs_query(c, ['3in', '100'])[0],
			plot_specs_query(c,[1000.0, 0.0, 10.0, 'default', 1.0])[0],
			user_info_query(c,['Stephani', 'Keefe', 'skeefe@ucdavis.edu'])[0]]
#print(type(inserter[6]))
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
