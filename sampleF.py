def lexsort_based(data):
  sorted_data = data[np.lexsort(data.T),:]
  row_mask = np.append([True],np.any(np.diff(sorted_data,axis=0),1))
  return sorted_data[row_mask]

'''
f_maps - list of feature maps
samples A & B at nearby pixel positions in f_maps
'''
def sampleF(f_maps, Nsamples, opts):
  sig = opts['sig']
  max_offset = 4*sig + 1
  im_size = f_maps.shape[:1]
  #draw pixels locations with equal probability without replacement
  yy = np.random.randint(0, im_size[0], size=Nsamples)
  xx = np.random.randint(0, im_size[1], size=Nsamples)
  p0 = np.concatenate((yy, xx), axis=1)
  p0 = lexsort_based(p0)
  Nsamples = p0.shape[0]
  #get random offset, add and sub
  r = np.random.normal(Nsamples, 2)
  r_n = np.divide(r, np.tile(np.sqrt(np.sum(np.pow(r, 2), axis=1)), (1, 2)))
  r = r + r_n
  s = np.sign(r)
  r = np.min(np.abs(r), max_offset)
  r = np.multiply(s, r)
  p1 = np.copy(p0)
  p2 = np.copy(p0)
  #remove out of bounds
  p1 = p1 + r
  p2 = p2 - r
  p1 = np.round(p1)
  p2 = np.round(p2)
  bool_mask = (p1[:, 0]<1) | (p1[:, 1]<1) | (p2[:, 0]<1) | (p2[:, 1]<1) | \
    (p1[:, 0]>im_size[0]) | (p1[:, 1]>im_size[1]) | (p2[:, 0]>im_size[0]) | (p2[:, 1]>im_size[1])
  p1 = np.delete(p1, bool_mask)
  p2 = np.delete(p2, bool_mask)
  #return to numbers in pixel array for both
  
  #for each feature map
  #access feature map by the numbers in each pixel array
  #order if model half space only
  for f_map in f_maps: