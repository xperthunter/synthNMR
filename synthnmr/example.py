import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg

limits = [0., 10.]
points = 10
variance = 1.0
grid_density = 100

x = np.linspace(limits[0], limits[1], grid_density)
y = np.linspace(limits[0], limits[1], grid_density)
x, y = np.meshgrid(x, y)
z = np.zeros((points, x.shape[1], x.shape[1]))

intv = limits[1] - limits[0]
variscale = intv*variance/100.

means = intv*np.random.sample((points, 2)) + limits[0]
varis = variscale*np.random.sample((points, 2))
uniform = np.full((points, 2), variscale)

print('Means:')
print(means)
print('Variances')
print(varis)
print('Variscale with variance = {}'.format(variance))
print(variscale)
print(uniform)

#for i, (cn, vn) in enumerate(zip(means, varis)):
#	fac = ((x - cn[0])**2/(2*vn[0])) + ((y - cn[1])**2/(2*vn[1]))
#	z[i,:,:] = np.exp(-fac)
#	
#z = np.sum(z,axis=0)
#
#for i, cn in enumerate(means):
#	fac = ((x - cn[0])**2/(2*variscale)) + ((y - cn[1])**2/(2*variscale))
#	z[i,:,:] = np.exp(-fac)
#
#z = np.sum(z,axis=0)
