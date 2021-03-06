import numpy as np
from getW import *
#from getE import *
from setEnvironment import *

def findBoundaries(image, _type=None, debug=False):
  if not _type:
    opts = setEnvironment('speedy')
  else:
    opts = setEnvironment(_type)
  image = np.uint8(image)
  if len(image.shape) == 2:
    image = np.expand_dims(image, 2)
  if image.shape[2] == 1:
    image = np.repeat(image, 3, axis=2)
  Ws, im_sizes = getW(image, opts)
  #E, E_oriented = getE(Ws, im_sizes, image, opts)
  #return E, E_oriented, Ws