import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import sys
import NMR_spectrum_generator_v2
import _pickle as cpickle

parser = argparse.ArgumentParser(description='Make a synthetic spectra database.')
parser.add_argument('--images', required=True, type=int,
    metavar='<int>', help='number of images you want to create (%(type)d)')
parser.add_argument('--imgsize', required=True, type=int, 
    metavar='<int>', help='square size of image in inches (%(type)d)')

arg = parser.parse_args()
print(arg)
print(arg.images)

#overlapped_spectra = np.zeros((10,450,450),dtype=np.uint8)
#resolved_spectra = np.zeros((10,450,450),dtype=np.uint8)
#centers = np.zeros((10,1),dtype=np.uint16)

#item = sys.argv[1]

#for i in range(10):
#	if i%100 == 0:
#		print(i)

#	pts = np.random.randint(40, 150,size=(1))
#	npts = pts[0]
#	xx,yy,zz,pps = NMR_spectrum_generator.peak_generator(points=npts,limits=[0.5,9.5], grid_density=300)
#	image_array, peak_array = NMR_spectrum_generator.spectra_generator(xx,yy,zz,pps)
#	overlapped_spectra[i,:,:] = image_array
#	resolved_spectra[i,:,:] = peak_array
#	centers[i,0] = np.uint16(npts)

#f = open("overlapped{}.dat".format(item), "wb")
#cpickle.dump(overlapped_spectra, f)
#f.close()
#f = open("resolved{}.dat".format(item), "wb")
#cpickle.dump(resolved_spectra, f)
#f.close()
#f = open("centers{}.dat".format(item), "wb")
#cpickle.dump(centers, f)
#f.close()
