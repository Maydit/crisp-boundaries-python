def borderSuppress(E_oriented):
  border_rad = np.ceil(0.03 * E_oriented.shape[0])
  xx, yy = np.meshgrid([list(range(len(E_oriented.shape[1]))), list(range(len(E_oriented.shape[0])))])
  aspect_ratio = E_oriented.shape[1] / E_oriented.shape[0]
  m1 = xx > aspect_ratio * yy
  m2 = np.fliplr(m1)
  #TODO border suppressor calculation

  norient = E_oriented.shape[2]
  dtheta = np.pi / norient
  ch_per = [4, 3, 2, 1, 8, 7, 6, 5]
  border_suppressor = [] #instead some numpy array
  for o in range(norient):
    theta = dtheta * o
    border_suppressor[:,:,ch_per[o]] = abs(cos(theta)).*hort_border_suppressor + abs(sin(theta)).*vert_border_suppressr
  border_suppressor = 1 - border_suppressor
  E_oriented = np.multiply(border_suppressor, E_oriented)
  return E_oriented