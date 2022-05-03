import numpy as np
from scipy import sparse
'''
returns pairs of nearby pixel positions in an image
'''
def getLocalPairs(im_size, rad, rad_inner, Nsamples):
  Npixels = np.prod(im_size)
  xx, yy = np.meshgrid(np.arange(0, 2*rad+1), np.arange(0, 2*rad+1))
  xx = xx-rad
  yy = yy-rad
  m = np.sqrt(np.power(xx, 2) + np.power(yy, 2)) <= rad
  m[rad, rad] = 0
  #since rad_inner = 0
  #m_inner = np.sqrt(np.power(xx, 2) + np.power(yy, 2)) <= rad_inner
  #m = m & !m_inner
  W = sparse.bsr_array((Npixels, Npixels))
  for i in range(-rad, rad+1):
    for j in range(-rad, rad+1):
      if m[i+rad,j+rad] and np.abs(i) <= im_size[1]:
        if i>=0:
          thing = np.vstack((np.ones((im_size[1]-i, 1)), np.zeros((i, 1))))
          d = np.tile(thing, (im_size[0], 1))
        else:
          thing = np.vstack((np.zeros((-i, 1)), np.ones((im_size[1]+i, 1))))
          d = np.tile(thing, (im_size[0], 1))
        d = np.roll(d, i, axis=1).T
        if (i + im_size[1]*j) >= 0 and (i + im_size[1]*j < Npixels):
          W = W + sparse.spdiags(d, i+im_size[1]*j, Npixels, Npixels)
  ii, jj, kk = sparse.find(W)
  ii = ii.astype(np.uint32)
  jj = jj.astype(np.uint32)
  m = ii>=jj
  ii = np.delete(ii, m)
  jj = np.delete(jj, m)
  if Nsamples:
    Nsamples = len(ii) if len(ii) <= Nsamples else Nsamples
    ii = np.random.choice(ii, Nsamples, replace=False)
    jj = np.random.choice(jj, Nsamples, replace=False)
  return ii, jj