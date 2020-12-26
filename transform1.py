import numpy as np
import cv2 
import math

def naive_image_rotate(image, degree):
    '''
    This function rotates the image around its center by amount of degrees
    provided.
    '''
    
    height = image.shape[0]
    width  = image.shape[1]

    midx,midy = (width//2, height//2)
    
    rads = math.radians(degree)

    rot_img = np.uint8(np.zeros(image.shape))

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
            y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)

            x=round(x)+midx 
            y=round(y)+midy 

            if (x>=0 and y>=0 and x<image.shape[0] and  y<image.shape[1]):
                rot_img[i,j,:] = image[x,y,:];

    return rot_img 

image = cv2.imread("lena.png")

rotated_image = naive_image_rotate(image,45)

cv2.imshow("original image", image)
cv2.imshow("rotated image",rotated_image)
cv2.waitKey(0)




