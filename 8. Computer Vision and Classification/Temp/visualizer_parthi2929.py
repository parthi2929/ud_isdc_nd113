"""
This snippet was created to visualize randomly all traffic signal images
Helps to arrive at interesting brightness values for feature extraction

THIS IS CREATED SPECIFICALLY TO BE USED IN IPYTHON NOTEBOOK

Author: parthi292929@gmail.com 
License: Please quote me.
Date: 7th Jun 2018
"""

#%matplotlib inline  # do this in ipython

from IPython.display import Image, display, HTML
#from loaders_parthi2929 import STANDARDIZED_LIST 
import matplotlib.pyplot as plt
from matplotlib import animation
import cv2
import numpy as np
from random import randint



nrows = 12
ncols = 5   
f, axArray = plt.subplots(nrows, ncols, figsize=(10,20))  # 12 rows, 5 cols
f.tight_layout()
plt.subplots_adjust(bottom=0.15, hspace=1)

def getSeparateLists(image_list):
    """
    Assuming list is standardized and having label attached to identify, 
    we will create 3 separate lists and send.
    NOTE LABEL STRIPPED AND ID ATTACHED
    """
    red_images = []    
    yellow_images = []
    green_images = []
    for index, each_image_label_pair in enumerate(image_list):  
        image = each_image_label_pair[0]
        label = each_image_label_pair[1]
        if label[0] == 1:
            red_images.append((image, index))
        elif label[1] == 1:
            yellow_images.append((image,index))
        else:
            green_images.append((image,index))
            
    return (red_images,yellow_images,green_images)

def getMaskedImage(image, label):
    """
    Returns the masked image as per label specified. For eg, label as 'Red' would 
    result in red areas extracted out of incoming image, and resultant image returned.
    NOTE INCOMING IMAGE IS RGB (if you used cv.imread,it would be BGR. I used matplotlib imread)
    """
    # first convert to HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    if label is 'red':
        red_mask_hsv1 = cv2.inRange(image_hsv, (0,30,50), (10,255,255))
        red_mask_hsv2 = cv2.inRange(image_hsv, (150,40,50), (180,255,255))
        mask_hsv = cv2.bitwise_or(red_mask_hsv1,red_mask_hsv2)
    elif label is 'yellow':
        mask_hsv = cv2.inRange(image_hsv, (10,10,110),(31,255,255))   
    else: # green
        mask_hsv = cv2.inRange(image_hsv,(43,40,120),(95,255,255)) 
        
    # standard mask operations to extract out specified label color
    mask_hsv = cv2.bitwise_not(mask_hsv)  # invert the mask
    masked_image = np.copy(image)
    masked_image[mask_hsv != 0] = [0, 0, 0] 
    
    return masked_image

def getHSVSum(image):
    """
    Input: RGB image (ensure, its not BGR)
    Output: HSV sums individually
    """
    # first convert to HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    # HSV channels
    h = image_hsv[:,:,0]
    s = image_hsv[:,:,1]
    v = image_hsv[:,:,2]
    h_sum = np.sum(h[:,:],axis=1)
    s_sum = np.sum(s[:,:],axis=1)
    v_sum = np.sum(v[:,:],axis=1)    
    
    return (h_sum, s_sum, v_sum)

# what if
def getHSVMax(image):
    """
    Input: RGB image (ensure, its not BGR)
    Output: HSV max individually
    """
    # first convert to HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    # HSV channels
    h = image_hsv[:,:,0]
    s = image_hsv[:,:,1]
    v = image_hsv[:,:,2]
    h_max = h.max(axis=1)
    s_max = h.max(axis=1)
    v_max = h.max(axis=1)    
    
    return (h_max, s_max, v_max)


# 723 to 757 is yellow 
def animate(frame_index):

    [axArray[i,j].clear() for i in range(0,nrows) for j in range(0,ncols)] 
    
    axArray[0,1].set_title('H Sum')
    axArray[0,2].set_title('S Sum')
    axArray[0,3].set_title('V Sum')    
    axArray[0,4].set_title('V Metrics')    
        
    
    # each label type would form 4 rows with 4 cols each
    # so below for loop is going to iterate 3 times, that is 'k' = 0,1,2
    nrows_1 = 4 # per image or per label 4 rows.         
    for k, each_list in enumerate(STANDARDIZED_DIVIDED_LIST):  
    
        #print(k, len(each_list))
    
        # get the image        
        num = randint(0, len(each_list)-1)  
        image = each_list[num][0]
        index = each_list[num][1]
    
        # crop it
        image = image[2:-2, 7:-7, :]    
        
        # always do this after crop
        (width,height,_) = image.shape
        area = width*height           
    
        # initialize axes
        axArray[k*nrows_1,0].set_title('ID: {}'.format(index))  
        #[axArray[i,j].set_ylim([width,0]) for i in range(0,nrows) for j in range(1,ncols)]    
        #[axArray[i,j].set_xlim([0,130]) for i in range(0,nrows) for j in range(1,ncols)]    
        
        # show original image
        axArray[k*nrows_1,0].imshow(image)
        
        # differentiate labels with bg color
        label_bg = ['#fbe9e7', '#fff9c4', '#e8f5e9']
        [axArray[i,j].set_facecolor(label_bg[k]) for i in range(k*nrows_1+1,k*nrows_1+4) for j in range(1,ncols)]        
        
        labels = ['red', 'yellow', 'green']
        for i in range(1,nrows_1):

            # per row operation
            label = labels[i-1]
            masked_image = getMaskedImage(image,label)        # masked image
            axArray[k*nrows_1+i,0].set_title(label + 'mask')    
            axArray[k*nrows_1+i,0].imshow(masked_image, cmap='gray')    
            
            hsv_sum = getHSVSum(masked_image)   # HSV sums of masked image
            
            # per cell operation
            for j in range(1,ncols-1):  # last col for V metrics
                
                # initialization
                axArray[k*nrows_1+i,j].set_ylim([0,width])
                axArray[k*nrows_1+i,j].set_xlim([0,130])
                
                summy = hsv_sum[j-1]
                summy_avg = summy/width                
                average = round(np.sum(summy)/area,1) # normalized avg across area                
                max_x = np.argmax(summy)
                #max_y = round(summy_avg[max_x],1)
                text = 'Avg B: ' + str(average) + '\nMax at: ' + str(max_x)
                
                # rotate to maka graph comparable to image
                x_new = np.linspace(0,len(summy_avg),len(summy_avg))
                axArray[k*nrows_1+i,j].invert_yaxis()
                axArray[k*nrows_1+i,j].plot(summy_avg, x_new)                                               
                #axArray[k*nrows_1+i,j].annotate(text,xy=(0.4, 0.5), xycoords="axes fraction")                            
                    
                # show only if curve is big enough
                #if average > 1:
                    #axArray[k*nrows_1+i,j].axhline(y=max_x, color='r')
                    
            # V metrics
            summy = hsv_sum[j-1]
            summy_avg = summy/width                
            average = round(np.sum(summy)/area,1) # normalized avg across area                
            max_x = np.argmax(summy)
            max_y = round(summy_avg[max_x],1)                       
            text = 'Avg: ' + str(average) + '\nMax: ' + str(max_y) + '\nMax at: ' + str(max_x)
            
            axArray[k*nrows_1+i,4].annotate(text,xy=(0.1, 0.2), xycoords="axes fraction")                                        
            
        
def visualize(STANDARDIZED_LIST):    
                    
    global STANDARDIZED_DIVIDED_LIST
    STANDARDIZED_DIVIDED_LIST = getSeparateLists(STANDARDIZED_LIST)
    anim = animation.FuncAnimation(f, animate, frames=10, interval=1000)

    plt.close()
    #HTML(anim.to_html5_video())
    return anim