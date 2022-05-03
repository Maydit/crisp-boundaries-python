import numpy as np
from orderAB import *

def lexsort_based(data):
  sorted_data = data[np.lexsort(data.T),:]
  row_mask = np.append([True],np.any(np.diff(sorted_data,axis=0),1))
  return sorted_data[row_mask]

'''
f_maps - NOT A LIST ANYMORE! Actually NxMxF
samples A & B at nearby pixel positions in f_maps
'''
def sampleF(f_maps, Nsamples, opts):
  sig = opts['sig']
  max_offset = 4*sig + 1
  im_size = f_maps.shape[:2]
  #draw pixels locations with equal probability without replacement
  yy = np.random.randint(0, im_size[0], size=Nsamples)
  xx = np.random.randint(0, im_size[1], size=Nsamples)
  p0 = np.vstack((yy, xx)).T
  p0 = lexsort_based(p0)
  Nsamples = p0.shape[0]
  #get random offset, add and sub
  r = np.random.normal(size=(Nsamples, 2)) * np.sqrt(sig)
  n = np.repeat(np.sqrt(np.sum(np.power(r, 2), axis=1))[:, np.newaxis], 2, axis=1)
  r_n = np.divide(r, n)
  r = r + r_n
  s = np.sign(r)
  r = np.minimum(np.abs(r), max_offset)
  r = np.multiply(s, r)
  p1 = np.copy(p0)
  p2 = np.copy(p0)
  #remove out of bounds
  p1 = p1 + r
  p2 = p2 - r
  p1 = np.round(p1).astype(np.int8)
  p2 = np.round(p2).astype(np.int8)
  bool_mask = (p1[:, 0]<0) | (p1[:, 1]<0) | (p2[:, 0]<0) | (p2[:, 1]<0) | \
    (p1[:, 0]>=im_size[0]) | (p1[:, 1]>=im_size[1]) | (p2[:, 0]>=im_size[0]) | (p2[:, 1]>=im_size[1])
  p1 = np.delete(p1, bool_mask, axis=0)
  p2 = np.delete(p2, bool_mask, axis=0)
  #return to numbers in pixel array for both
  #pain
  ii = np.ravel_multi_index([p1[:,0], p1[:,1]], im_size)
  jj = np.ravel_multi_index([p2[:,0], p2[:,1]], im_size)
  F = np.zeros((p1.shape[0], f_maps.shape[2] * 2))
  #for each feature map
  #access feature map by the numbers in each pixel array
  for i in range(f_maps.shape[2]):
    tmp = np.ravel(f_maps[:,:,i], 'F') #because thats how they do it in the matlab
    F[:, i] = tmp[ii]
    F[:, i + f_maps.shape[2]] = tmp[jj]
  #order if model half space only
  if opts['model_half_space_only']:
    F = orderAB(F)
  print(F.shape)
  return F