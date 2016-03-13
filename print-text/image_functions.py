# this will be a module with a bunch of functions for applying filters and what
# not to images 
# all the input to functions should be an np array
# all the functions should return a list of the new images
from scipy.misc import imread, imsave
from scipy import ndimage
import numpy as np

def rotations(img):
    return [ndimage.rotate(img,i,mode='nearest') for i in np.arange(30.0, 50.0, 2)]
def fourier(img,size=100):
    return [ndimage.fourier_ellipsoid(img,size),
            ndimage.fourier_shift(img,size),
            ndimage.fourier_uniform(img,size)]
def filters(img,size=100):
    l = [ndimage.gaussian_filter(img, i) for i in np.arange(0,4,0.5)] + \
        [ndimage.maximum_filter(img, i) for i in np.arange(1,4,0.2)] + \
        [ndimage.median_filter(img, i) for i in np.arange(1,4,0.2)] + \
        [ndimage.minimum_filter(img, i) for i in np.arange(1,4,0.2)]
    return l
            
def zoom(img,size=100):
    return [ndimage.zoom(img, i) for i in np.arange(1,5,0.5)]
def get():
    return [rotations,filters]
