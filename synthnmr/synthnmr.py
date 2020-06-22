"""
synthnmr.py
~~~~~~~~~~~

A module for making and storing synthetic nmr experiments.
"""

# Standard libraries
import sqlite3
import io
import os
import re

# Third-party libraries
import numpy as np

"""
Generator Functions
"""

def random_spectrum(points=100,
					limits=[0,10],
					grid_density=1000,
					max_variance=1.0,
					min_variance=1.0):

	"""
	Generates 2D Gaussian peaks in a specified x/y window.

	Parameters
	----------
	+ points		`int` number of peaks
	+ limits		`list` upper/lower limits for x/y axes
	+ grid_density	`int` discretization for both dimensions
	+ max_variance	`float` max variance as % of interval size
	+ min_variance	`float` min variance as % of interval size

	Notes
	-----
	+ Default max_variance and min_variance are equal. By default, generated
		peaks will all have same size.

	Returns
	-------
	+ xyz			numpy `stack`, dim(grid_density, grid_density, 3).
					Order (x,y,z).
	+ points_info	numpy `array`, dim(points, 4). First 2 cols = center coords.
					Last 2 columns = variances in x/y.
	"""
	# Asserts
	assert(points > 1)
	assert(len(limits) == 2)
	assert(grid_density > 1)
	assert(max_variance >= min_variance)

	# Prepare numpy arrays
	x    = np.linspace(limits[0], limits[1], grid_density)
	y    = np.linspace(limits[0], limits[1], grid_density)
	x, y = np.meshgrid(x, y)
	z    = np.zeros((points, x.shape[1], x.shape[1]))
	size = limits[1] - limits[0]

	# Handle variances
	if max_variance == min_variance:
		variscale = size*max_variance/100.
		varis = np.full((points, 2), variscale)
	else:
		dv = (max_variance - min_variance)*size/100.
		varis = dv*np.random.sample((points, 2)) + min_variance*size/100.

	# Construct centers
	means = size*np.random.sample((points, 2)) + limits[0]

	# Build all the peaks
	for i, (cn, vn) in enumerate(zip(means, varis)):
		fac = ((x - cn[0])**2/(2*vn[0])) + ((y - cn[1])**2/(2*vn[1]))
		z[i,:,:] = np.exp(-fac)

	# Package all the results
	z = np.sum(z,axis=0)
	xyz = np.stack((x,y,z), axis=2)
	points_info = np.concatenate((means, varis), axis=1)
	return xyz, points_info

def spectrum_frompts(pts=[],input="",
					 max_variance=1.0,
					 min_variance=1.0,
					 grid_density=1000):
	for x, y in pts:
		xyz[i,:,:] = np.exp(-(x-grid)**2 + (y-grid)**2)
	pass

def transformed_spectrum():
	pass

def protein_spectrum():
	pass

"""
Database Insertion Methods
"""

def init(location=""):
	"""
	Initialize a synthnmr database file.

	"""
	assert(location)
	module_path = os.path.abspath(os.path.dirname(__file__))
	sql_path = os.path.join(module_path, '../sql/synth_schema.sql')

	conn = sqlite3.connect(location)
	c = conn.cursor()
	with open(sql_path) as fp:
		c.executescript(fp.read())

	conn.commit()
	conn.close()
	return

### All table insert methods ###



def img_specs_inserter(cursor, figsize, dpi):
	"""
	Inserts figsize and dpi into img_specs table

	Parameters
	----------
	+ figsize	`str`
	+ dpi		`int`

	"""
	check_dpi = isinstance(dpi, str)

	if (isinstance(figsize, str)) == True:
		check = re.match(r"\d+inch|\d+in", figsize) ###
		if check is not None and check_dpi == True:
			img_sql = ((f'INSERT INTO img_specs (figsize, dpi) VALUES (?, ?)'))
		else:
			pass
	else:
		pass

	img_list = [figsize, dpi]
	cursor.execute(img_sql, img_list)



def plot_specs_inserter(cursor, density, lower_limit, upper_limit, mode, variance):
	"""
	Inserts density, lower_limit, upper_limit, mode, variance into plot_specs table

	Parameters
	----------
	+ density       `int`
	+ lower_limit	`float`
	+ upper_limit	`float`
	+ mode          `str`
	+ variance      `float`
	"""
	assert(isinstance(density, int))
	assert(isinstance(lower_limit, float))
	assert(isinstance(upper_limit, float))
	assert(isinstance(mode, str))
	assert(isinstance(variance, float))

	plot_sql = ''.join((f'INSERT INTO plot_specs (density, lower_limit, upper_limit, mode, ',
					'variance) VALUES (?, ?, ?, ?, ?)'))

	plot_list=[density, lower_limit, upper_limit, mode, variance]

	cursor.execute(plot_sql, plot_list)


def user_info_inserter(cursor, first_name, last_name, email):
	"""
	Inserts first_name, last_name, email into user_info table

	Parameters
	----------
	+ first_name	`str`
	+ last_name		`str`
	+ email			`str`
	"""
	check_fn = isinstance(first_name, str)
	check_ln = isinstance(last_name, str)
	check_em = isinstance(email, str)

	if check_em == True:
		email_check = re.search(r"\@\w+\.\w+", email)
		if email_check is not None and check_ln == True and check_fn == True:
			user_sql = ((f'INSERT INTO user_info (first_name, last_name, email) VALUES (?, ?, ?)'))
		else:
			pass
	else:
		pass
	#z = re.match(pattern, email)
	#if z == True:
	#	pass
	#else:
	#	pass
	user_info_list = [first_name, last_name, email]

	cursor.execute(user_sql, user_info_list)



def insert(dbfile=""):

	try:
		conn = sqlite3.connect(dbfile)
		c = conn.cursor()
	except:
		init(location = dbfile)
		conn = sqlite3.connect(dbfile)
		c = conn.cursor()

	# img_specs insert
	# plot_specs insert
	# data insert

"""
Query functions
+ read in query statements: either has sql or from yaml form?
n=10 # number of results
id=100..1000 # records with id between 100 and 1000
mode=random,frompts # records made with modes random and frompts
density=1000
limits=[-5,5]
protein=1GAF
"""

"""
Utility functions
+ generate tsv
+ generate yaml
+ making images -- visualization purposes
+ summary -- summarize a db -- how many records, number of unique experiments
"""











