import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

'the function that creates peaks'
def peak_generator(points=100, limits=[0,10], grid_density=1000, mode="default", variance=1.0): #As I understand it, we have 100 points, which we wilimits  when generating the peaks; however, I am not too sure about the limits. Do the limits constraint the points within that specific graph? Also, could you explain what does "mode" variable actually do?
    ##### Keith comments
    # Limits are just what are limits for the numbers we are graphing, sometimes we might want to plot a spetrum where the axes are [-1,1] and [-1,1]. The way python works here are arguments are given default values. When we write 'points=100' in the function definition above, we are saying the variable points is assigned a default value of 100. This way when we call it in an outside script we can just write peak_generator() and give no arguments because we assign default values. We can equally do peak_generator(points=20) plotting 20 points instead of 100.
    # Mode will be used for the different types of plots we want to do. Sometimes we will want to do the 2D gaussian approach, others we will use other approaches. So mode is more of a place holder for different types of methods we want to use in plotting. 
    #####
    x = np.linspace(limits[0], limits[1], grid_density) 
    y = np.linspace(limits[0], limits[1], grid_density) #In these two lanes we are creating x and y axis, correct? ### Yes
    x, y = np.meshgrid(x, y)
    z = np.zeros((points, x.shape[1], x.shape[1])) '(shape, type, order)' #why did you set type and order to x.shape[1] 
    ##### 
    # Its not, i only give shape. The three values are in parenthesis together, and its the three together that define the shape of zeros. 
    #####
    if mode == "default": #why is it so important to have mode in default?
    #                     ##### Its not, its just checking if it is default 
        intv = limits[1] - limits[0] #setting the interval, that is the difference of two limits? 
                          ##### Yes
        means = intv*np.random.sample((points, 2)) + limits[0]' multiplying the interval with the numpy.random.sample(100,1) + limits[0]' #by doing so, do we just spread the 100 points we have around the graph? why do we need to add limits to this function?
        ##### Yes, randomly picking them around the graph. Because np.random.sample is picking random numbers between [0,1]. But we want random numbers selected inside our limits. What I have above is how it works. 
        variscale = intv*variance/100. 
        varis = variscale*np.random.sample((points, 2)) #how is varis different from means? in other words, what does varis do and what does means specifically do in this function?
        ##### Means are the centers of points. varis is the variance for the 2D gaussian at each point. 
        for i, (cn, vn) in enumerate(zip(means, varis)): 
            fac = ((x - cn[0])**2/(2*vn[0])) + ((y - cn[1])**2/(2*vn[1])) #would it be okay for you to write what the following variables are: cn and vn?
            ##### through the loop we need the center and variance for each points. cn is the coordinates for the center of the point, and vn is the variance in x- and y- directions for each point.  
            z[i,:,:] = np.exp(-fac)
        z = np.sum(z,axis=0)
    else:
        pass
    return x, y, z, means, varis

'function that generates spectra'
def spectra_generator(x, y, z, centers, figsize=3, dpi=100, specfile="100.png", resfile="100-r.png"): 'dpi = dots pe inch = how many poxels the figure comprises
    fig = plt.figure(figsize=(figsize,figsize), dpi=dpi,frameon=False)'figsize = (3,3)
    canvas = FigureCanvasAgg(fig) #are such things as FigureCanvasAgg, add_plot are part of the matplolib? 
    ##### It is in the import at the top, but yes
    ax = fig.add_subplot(111)
    fig.tight_layout()
    fig.subplots_adjust(left=0.0,right=1.0,top=1.0,bottom=0.0,hspace=0.0,wspace=0.0)
    ax.axes.get_xaxis().set_visible(False) 
    ax.axes.get_yaxis().set_visible(False)
    ax.contourf(x,y,z, 100, cmap="gray")
    ax.axis('off')
    fig.savefig(specfile, bbox_inches='tight', pad_inches=0.0)
    fig.canvas.draw()
    s, (width, height) = canvas.print_to_buffer()
    X = np.frombuffer(s, np.uint8).reshape((height, width, 4))
    X = X[:,:,1]
    plt.close()
    #setting the graph 
    
    fig1 = plt.figure(figsize=(figsize,figsize), dpi=dpi,frameon=False)
    canvas1 = FigureCanvasAgg(fig1)
    ax1 = fig1.add_subplot(111)
    fig1.tight_layout()
    fig1.subplots_adjust(left=0.0,right=1.0,top=1.0,bottom=0.0,hspace=0.0,wspace=0.0)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.plot(centers[:,0], centers[:,1],'ko',markersize=2)
    ax1.axis('off')
    fig1.savefig(resfile, bbox_inches='tight', pad_inches=0.0)
    fig1.canvas.draw()
    s, (width, height) = canvas1.print_to_buffer()
    X1 = np.frombuffer(s, np.uint8).reshape((height, width, 4))
    X1 = X1[:,:,1]
    plt.close()
    return X, X1

"""plt.ioff()
xx, yy, zz, pps = peak_generator(points=50,limits=[0.5,9.5], grid_density=500)
image_array, peak_array = spectra_generator(xx,yy,zz,pps)
"""
