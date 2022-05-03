import time

def getE(Ws, im_sizes, image, opts):
  if opts['globalization_method'] == 'spectral_clustering':
    if opts['display_progress']:
      print('\nspectral clustering...')
      op_time = time.time()
    nvec = opts['spectral_clustering']['nvec']
    if len(im_sizes) > 1:
      #todo
      pass
    else:
      W = Ws[0]
      if not opts['spectral_clustering']['approximate']:
        #E_oriented = spectralPb_custom(W, [im_sizes[0] ], '', nvec)
        #TODO fix the above line
      else:
        E_oriented = spectralPb_fast_custom(W, [], nvec)
        #TODO fix the above line
    if opts['display_progress']:
      op_time = time.time() - op_time
      print('done: {op_time:.2f} sec\n')
  else:
    raise ValueError(f'Unknown globalization method {opts['globalization_method']}')
  if opts['border_suppress']:
    E_oriented = borderSuppress(E_oriented)
  E = np.amax(E_oriented, axis=2) #get largest elements along dimension 2
  return E, E_oriented