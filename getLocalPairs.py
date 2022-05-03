import numpy as np
'''
returns pairs of nearby pixel positions in an image
'''
def getLocalPairs(im_size, rad, rad_inner, Nsamples):
  '''Npixels = np.prod(im_size)
  xx, yy = np.meshgrid(np.arange(0, 2*rad+1), np.arange(0, 2*rad+1))
  xx = xx-rad-1
  yy = yy-rad-1
  m = np.sqrt(np.pow(xx, 2) + np.pow(yy, 2)) <= rad
  m[rad, rad] = 0
  #since rad_inner = 0
  #m_inner = np.sqrt(np.pow(xx, 2) + np.pow(yy, 2)) <= rad_inner
  #m = m & !m_inner
  W = np.zeroes(Npixels, Npixels)
  for i in range(-rad, rad+1):
    for j in range(-rad, rad+1):
      if m[i+rad,j+rad]:
        if i>=0:
          d = 'fuckery'
        else:
          d = 'other thing'
        d = circshift(d, i)
        if (i + im_size[1]*j) > 0 and (i + im_size[1]*j < Npixels):
          W = W + spdiags(d, i+im_size[1]*j, Npixels, Npixels)
  ii, jj = find(W)
  
  return ii, jj
  '''
  #Gonna do it custom cause I can't be asked
  #sample first point
  #sample second point less than 5 euclidean distance
  return ii, jj