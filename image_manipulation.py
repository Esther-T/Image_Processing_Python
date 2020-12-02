# Image Processing using Numpy and Scipy

from scipy import misc
from scipy import ndimage
import imageio
import matplotlib.pyplot as plt
f = misc.face()
IMAGE_PATH = r'C:\Users\lin.tan\Git\Image_Processing\grapefruit.jpg'
imageio.imsave(IMAGE_PATH, f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()

# Creating a numpy array from an image
imageio.imsave(IMAGE_PATH, f) # First we need to create the PNG file

f = imageio.imread(IMAGE_PATH)
print(type(f))
print(f.shape, f.dtype)

# Edit Images, convert to a grayscale image
f = misc.face(gray=True)
plt.imshow(f, cmap=plt.cm.gray)
plt.show()

# Playing with contrast with max and min values
plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=400)
plt.axis('off')
plt.show()
plt.contour(f, [50,200])
plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='bilinear')
plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='nearest')  

# Sharpening a blurry image
f = misc.face(gray=True)
blurred_f = ndimage.gaussian_filter(f, sigma=3)
f = misc.face(gray=True).astype(float)
blurred_f = ndimage.gaussian_filter(f, 3)
filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
alpha = 30
sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
plt.imshow(sharpened)
plt.show()