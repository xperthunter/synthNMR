"""
synthnmr.py
~~~~~~~~~~~

A module for making and storing synthetic nmr experiments. 
"""

# Standard libraries
import sqlite3
import io

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

# maybe but the generator here?

def gen(**kwargs):
	mode = kwargs['mode']
	n    = kwargs['n']
	vari = kwargs['variance']
	
	
# read in a yaml file or dictionary?
# do that processing in synthnmr?

def add(**kwargs):
	pass
	
def query(**kwargs):
	pass