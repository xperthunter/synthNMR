'''
Peak and spectra generators. 
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

def peak_generator(
	points=100, 
	limits=[0,10], 
	grid_density=1000, 
	mode="default", 
	variance=1.0):
	'''
	Generates 2D Gaussian peaks in a specified x/y window. 
	
	Parameters
	----------
	+ points		Number of peaks you want in the spectrum.
	+ limits		Numeric range of x/y limits. Window is a always square.
	+ grid_density	Number of points in each dimension.
	+ mode			mode for placing peaks in spectrum. Current implemented modes:
						+ default	Peaks randomly placed, random variances
						+ uniform	Peaks randomly placed, same variance
	+ variance		Variance of gaussian peaks in spectrum. Variance is a percentage of
						the interval size.  
						
	Returns
	-------
	    
	'''
	x = np.linspace(limits[0], limits[1], grid_density)
	y = np.linspace(limits[0], limits[1], grid_density)
	x, y = np.meshgrid(x, y)
	z = np.zeros((points, x.shape[1], x.shape[1]))
	intv = limits[1] - limits[0]
	variscale = intv*variance/100.
	
	if mode == "default":
		means = intv*np.random.sample((points, 2)) + limits[0]
		varis = variscale*np.random.sample((points, 2))
		for i, (cn, vn) in enumerate(zip(means, varis)):
			fac = ((x - cn[0])**2/(2*vn[0])) + ((y - cn[1])**2/(2*vn[1]))
			z[i,:,:] = np.exp(-fac)
		
		z = np.sum(z,axis=0)
		
		xyz = np.stack((x,y,z), axis=2)
		return xyz, means, varis
	
	elif mode == "uniform":
		means = intv*np.random.sample((points, 2)) + limits[0]
		for i, cn in enumerate(means):
			fac = ((x - cn[0])**2/(2*variscale)) + ((y - cn[1])**2/(2*variscale))
			z[i,:,:] = np.exp(-fac)
			
		z = np.sum(z,axis=0)
		varis = np.full((points,2), variscale)
		xyz = np.stack((x,y,z), axis=2)
		return xyz, means, varis


def spectra_generator(xyz, 
					  centers, 
					  figsize=3, 
					  dpi=100):
	'''
	Generates images of gaussian peaks. 
	
	Parameters
	----------
	+ xyz		
	+ centers
	+ figsize
	+ dpi
	
	Returns
	-------
	'''
	fig = plt.figure(figsize=(figsize,figsize),dpi=dpi,frameon=False)
	canvas = FigureCanvasAgg(fig)
	ax = fig.add_subplot(111)
	fig.tight_layout()
	fig.subplots_adjust(left=0.0,right=1.0,top=1.0,bottom=0.0,hspace=0.0,wspace=0.0)
	ax.axes.get_xaxis().set_visible(False)
	ax.axes.get_yaxis().set_visible(False)
	ax.contourf(xyz[:,:,0],xyz[:,:,1],xyz[:,:,2], 100, cmap="gray_r")
	ax.axis('off')
#	buf = io.BytesIO()
#	fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.0)
#	buf.seek(0)
	fig.canvas.draw()
	s, (width, height) = canvas.print_to_buffer()
	X = np.frombuffer(s, np.uint8).reshape((height, width, 4))
	X = X[:,:,1]
	plt.close(fig)
	
	fig1 = plt.figure(figsize=(figsize,figsize), dpi=dpi,frameon=False)
	canvas1 = FigureCanvasAgg(fig1)
	ax1 = fig1.add_subplot(111)
	fig1.tight_layout()
	fig1.subplots_adjust(left=0.0,right=1.0,top=1.0,bottom=0.0,hspace=0.0,wspace=0.0)
	ax1.axes.get_xaxis().set_visible(False)
	ax1.axes.get_yaxis().set_visible(False)
	ax1.plot(centers[:,0], centers[:,1],'ko',markersize=2)
	ax1.axis('off')
#	buf1 = io.BytesIO()
#	fig1.savefig(buf1, format='png', bbox_inches='tight', pad_inches=0.0)
#	buf1.seek(0)
	fig1.canvas.draw()
	s, (width, height) = canvas1.print_to_buffer()
	X1 = np.frombuffer(s, np.uint8).reshape((height, width, 4))
	X1 = X1[:,:,1]
	plt.close(fig1)
	return X, X1
	
"""plt.ioff()
xx, yy, zz, pps = peak_generator(points=50,limits=[0.5,9.5], grid_density=500)
image_array, peak_array = spectra_generator(xx,yy,zz,pps)
"""