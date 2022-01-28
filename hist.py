import numpy as np
from matplotlib import pyplot as plt
from PIL import Image as im
  
# reading the image and store it in img object
img = im.open('c:\\Users\\User\\Downloads\\black.jpg')

#disply the image by img object
img.show()

#convert image to array
img_to_array = np.asarray(img)  

#convert array to flat array
img_to_flatarray=img_to_array.flatten() 
#print(img_to_flatarray)

#count no of occurances of each value in array
array_hist = np.bincount(img_to_flatarray, minlength=256) 
#print(array_hist)

#find the total no of pixels
total_pixel = np.sum(array_hist)
#print(total_pixel)

# normalizing the values by dividing with total no. of pixels
array_hist = array_hist/total_pixel

# finding the cumulative sum
cumulative_array = np.cumsum(array_hist)
#print(cumulative_array)

# multiply by maximum grey level and round off the values by taking its floor
transform = np.floor(255 * cumulative_array).astype(np.uint8)
#print(transform)

#convert 1D array to 1D list
list_image = list(img_to_flatarray ) 
#print(list_image)

#we transform pixel values so that  we can  eqalise
equalise_list = [transform[k] for k in list_image]

# reshaping the array and write into another object
equalise_img_array = np.reshape(np.asarray(equalise_list), img_to_array.shape)

# convert the array to image  
final_img=im.fromarray(equalise_img_array)

# we now save the file in the location we want
final_img.save('c:\\Users\\User\\Downloads\\final_image.jpg')


#calculating  histogram  of equalized image

#count no of occurances of each value in array
equalized_histogram_array = np.bincount(equalise_img_array.flatten(), minlength=256)


#find the total no of pixels
total2_pixels = np.sum(equalized_histogram_array)

# normalizing the values by dividing with total no. of pixels
norm_values = equalized_histogram_array/total2_pixels

# finding the cumulative sum
cum_sum2 = np.cumsum(norm_values)

#now we plot the histogram before and after eqqualization

#plt histogram before equalization
plt.figure()
plt.plot(array_hist)
plt.title("BEFORE EQUALIZATION")
plt.xlabel('pixel intensity ')
plt.ylabel('distribution')

#plot histogram after equalization
plt.figure()
plt.plot(norm_values)

plt.title("AFTER EQUALIZATION")
plt.xlabel('pixel intensity')
plt.ylabel('distribution')

imgfinal = im.open('c:\\Users\\User\\Downloads\\final_image.jpg')

#showing the final image after the histogram equalization
imgfinal.show()


