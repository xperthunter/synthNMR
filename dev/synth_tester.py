#!/usr/bin/env python3
import NMR_spectrum_generator_v2 as gen
import matplotlib.pyplot as plt
xx, yy, zz, mm, vv = gen.peak_generator(points=50,limits=[0.5,9.5],grid_density=500)

img, peaks = gen.spectra_generator(xx, yy, zz, mm)

plt.imshow(img)



plt.imshow(peaks)
