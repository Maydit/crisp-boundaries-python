import numpy as np
import cv2
from scipy.ndimage import generic_filter
from sklearn.decomposition import PCA

def mat2gray(image):
  cv2.normalize(image, image, np.min(image), np.max(image), cv2.NORM_MINMAX)
  image = np.uint8(image)
  return image

#no idea if this works as intended...
def pcaIm(image):
  im_size = image.shape[:1]
  X = np.reshape(image, (image.shape[0] * image.shape[1], image.shape[2]))
  pca = PCA()
  Y = pca.score(X)
  im = np.reshape(Y, (im_size, image.shape[2]))
  return im

'''
in -
im_rgb - NxMx3 
scale -  how many times to downsample?
which_feature - which feature type to compute
opts - params

out - 
f_maps NxMxF feature maps
'''
def getFeatures(im_rgb, scale, which_feature, opts):
  if which_feature == 'luminance':
    im = mat2gray(np.mean(im_rgb, 2))
  elif which_feature == 'color':
    if im_rgb.shape[2] == 3:
      cf = mat2gray(cv2.cvtColor(im_rgb, cv2.COLOR_RGB2LAB))
      im = cf
    elif im_rgb.shape[2] == 1:
      im = im_rgb
    else:
      raise ValueError('unhandled image format')
  elif which_feature == 'var':
    f = pcaIm(im_rgb) #i cant figure out what this is supposed to do
    Nhood_rad = 2**(scale - 1)
    se = cv2.getStructuingElement(cv2.MORPH_ELLIPSE, (Nhood_rad * 2, Nhood_rad * 2))
    #se = strel('disk',Nhood_rad, 0)
    vf = mat2gray(np.sqrt(generic_filter(f, np.std, footprint=se)))
    im = vf
  else:
    raise ValueError(f'feature type {which_feature} not recognized')
  width = im.shape[1] * 2**(-(scale - 1))
  height = im.shape[0] * 2 **(-(scale - 1))
  im = cv2.resize(im, (width, height))
  if opts['features']['decorrelate']:
    im = mat2gray(pcaIm(im))
  f_maps = im
  return f_maps