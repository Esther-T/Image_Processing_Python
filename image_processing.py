# Image Processing using Python OpenCV
import cv2 as cv
import matplotlib.pyplot as plt

IMG_PATH = r"C:\Users\lin.tan\Pictures\Saved Pictures\test.jpg"
imgArray = cv.imread(IMG_PATH)

# with OpenCV, image will appear in BGR mode instead of RGB
plt.imshow(imgArray)
plt.show()

# converts image from BGR to RGB
convertedArray = cv.cvtColor(imgArray, cv.COLOR_BGR2RGB)
plt.subplots(figsize=(15,10))
plt.imshow(convertedArray)
plt.show()

# display images in the R,G,B channels separately
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(14,10))

ax1.imshow(convertedArray[:,:,0], cmap="Reds_r")
ax1.set_title("Red, R", size=20)
ax1.imshow(convertedArray[:,:,1], cmap="Greens_r")
ax1.set_title("Green, G", size=20)
ax1.imshow(convertedArray[:,:,2], cmap="Blues_r")
ax1.set_title("Blue, B", size=20)
ax4.axis("off")
plt.tight_layout()
plt.show()

# show the histograms for R,G,B
fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,4))
ax1.hist(convertedArray[:,:,0].flatten(), color="Red", bins=200)
ax1.set_title("Red, R", size=20)
ax2.hist(convertedArray[:,:,1].flatten(), color="Green", bins=200)
ax2.set_title("Green, G", size=20)
ax3.hist(convertedArray[:,:,2].flatten(), color="Blue", bins=200)
ax3.set_title("Blue, B", size=20)
plt.tight_layout()
plt.show()

# Analyze the bit depth
type(convertedArray) # numpy.ndarray
print(convertedArray.dtype) # dtype(uint8)
# clearest pixel: 255 and darkest pixel: 0
print (convertedArray.min())
print (convertedArray.max())

# Crop Images
print(convertedArray.shape) # geometric size (900, 1200 , 3)
# rows= 900, columns= 1200, channels= 3 (R,G,B)
crop1 = convertedArray[:200,:300, :] # Remove first 200 rows and 300 columns
crop1.shape
plt.imshow(crop1)
plt.show()
# If we want to select from row 600 to 900, column 350 to 1200 and all channels
crop2 = convertedArray[600:900,350:1200,:]
plt.figure(figsize=(15,8))
plt.imshow(crop2)
plt.show()
# If we want to crop only one channel
plt.figure(figsize=(15,8))
plt.imshow(convertedArray[600:900,350:1200,0], cmap="Greys_r")
plt.show()

# get total number of pixels in the image
# multiple number of pixels on the long side by num pixels on short side
print(convertedArray.shape[0]* convertedArray.shape[1])

# extract a vertical and a horizontal section from the image
plt.subplots(figsize=(15,10))
plt.imshow(convertedArray)
plt.axvline(1000, color="yellow") # draw a line from x=1000
plt.axhline(600, color="orange") # draw a line from y=600
plt.show()

# extract the two profiles
verSection = convertedArray[:,1000,:]
plt.figure(figsize=(16,5))
plt.plot(verSection[:,0], label="Red", color="#e74c3c")
plt.plot(verSection[:,1], label="Green", color="#16a085")
plt.plot(verSection[:,2], label="Blue", color="#3498db")
plt.xlabel("X")
plt.legend()
plt.show()

