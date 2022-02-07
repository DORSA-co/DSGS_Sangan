import models
import numpy as np
import tensorflow as tf
import cv2
import json

#this function build model and load weights
def load_model():
    model = models.resnet_unet2( (640,960,1) )
    model.load_weights('model.h5')
    return model


def filter_stone(max_area,min_area, mask):
        def func(x):
            if min_area < cv2.contourArea(x) < max_area:
                cx = (np.min(x[:,:,0]) + np.max(x[:,:,0]))/2
                cy = (np.min(x[:,:,1]) + np.max(x[:,:,1]))/2
                cx = int(cx)
                cy = int(cy)
                roi = mask[cy-2:cy+3, cx-2:cx+3]
                if roi.mean()>250:
                    return True
            return False
        return func 




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
model = load_model()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def stone_detection(input_imgs, code='0000'):
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #model = load_model()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    
    #conver images to array
    
    input_imgs = np.array( input_imgs, dtype=np.uint8)
    
    # imgs should be ( number img, h, w) o.w if img is just (h,w) we convert it to (1,h,w)
    if len(input_imgs.shape)==2:
        input_imgs = np.expand_dims( input_imgs, 0)
        
    #input model size is (640,960) so imgs should be resize
    resize_imgs = []
    for img in input_imgs:
        img = cv2.resize(img, (960,640))
        resize_imgs.append(img)
        
    inputs = np.array( resize_imgs, dtype=np.float32)
    
    
    #for deep model input shooud be (batch numbr, h,w,1)
    inputs = np.expand_dims(inputs, axis=-1)
    
    #normal imgs
    inputs = inputs/255.
    
    
    outs = model.predict(inputs)[0]
    #make predict model binary
    thresh=0.3
    outs[outs>=thresh]= 1
    outs[outs<thresh] = 0
    
    #conver to opencv image format
    outs=outs * 255
    outs = outs.astype(np.uint8)
    outs = cv2.bitwise_not(outs)
    #cv2.imshow('mask',outs)
    #cv2.waitKey(0)
    
    #some morphology filter for better output
    outs = cv2.erode(outs,np.ones((3,3)))
    outs = cv2.dilate(outs,np.ones((3,3)))
    
    #resize to orginal
    outs = cv2.resize(outs,(1920,1200))
    _,outs = cv2.threshold(outs,50,255,cv2.THRESH_BINARY)
    
    #finde contours
    cnts,h= cv2.findContours(outs, cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
     
    
                
    
    
    min_area = 5000       
    max_area=100000  
    #filter by area and accept only white stone in mask  
    res_cnts = list(filter(filter_stone(max_area, min_area, outs) ,cnts))
    
    print(len(res_cnts))
    res_img = cv2.drawContours(input_imgs[0], res_cnts, -1, (255), 10)
    #cv2.imshow('res', res_img)
    #cv2.waitKey(0)
    
    stones_dict = {}
    info_dict = {}
    
    #make stone json
    for i,cnt in enumerate(res_cnts):
        x,y,w,h = cv2.boundingRect(cnt) #calc contour bonding box
        
        stone_dict = {}
        stone_name = 'stone{}'.format(i+1)
        
        stone_dict['contour'] = cnt.reshape((-1,2)).tolist()
        stone_dict['area'] = cv2.contourArea(cnt)
        stone_dict['length'] = h
        stone_dict['width'] = w
        stones_dict[stone_name] = stone_dict
        
    #make info json
    info_dict['count'] = len(res_cnts)
    info_dict['code'] = str(code)
    
    #write Jsones
    
    with open('info.json', 'w') as file:
        json.dump(info_dict,file)
        
    with open('stones.json', 'w') as file:
        json.dump(stones_dict,file)
    
    return True
        
    
    
    
    

'''
if __name__ == '__main__':
    img = cv2.imread('1.tiff',0)
    print(stone_detection(img,'a123'))
'''