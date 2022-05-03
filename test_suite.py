from getLocalPairs import *
from findBoundaries import *
import cv2

if __name__ == '__main__':
  image = cv2.imread('images/test.png', cv2.IMREAD_COLOR)
  #image = cv2.imread('images/logo.png', cv2.IMREAD_COLOR)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  findBoundaries(image)
  #image = np.array([[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]])
  #image = np.repeat(image[:,:,np.newaxis], 3, axis=2)
  #print(image[:,:,0])
  #opts = {'sig': 0.25, 'model_half_space_only': True}
  #print(sampleF(image, 100, opts))
  #im_size = (4, 4)
  #getLocalPairs(im_size, 5, 0, 100)