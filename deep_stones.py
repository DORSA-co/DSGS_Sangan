import os
import models
import numpy as np
import tensorflow as tf
import cv2
import json
import time
# this function build model and load weights

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


def load_model():
    model = models.resnet_unet((640, 960, 1))
    model.load_weights('model.h5')
    return model


def filter_stone(max_area, min_area, mask):
    def func(x):
        if min_area < cv2.contourArea(x) < max_area:
            cx = (np.min(x[:, :, 0]) + np.max(x[:, :, 0]))/2
            cy = (np.min(x[:, :, 1]) + np.max(x[:, :, 1]))/2
            cx = int(cx)
            cy = int(cy)
            roi = mask[cy-2:cy+3, cx-2:cx+3]
            if roi.mean() > 250:
                return True
        return False
    return func


def stone_detection(input_imgs):
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #model = load_model()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # conver images to array

    input_imgs = np.array(input_imgs, dtype=np.uint8)

    # imgs should be ( number img, h, w) o.w if img is just (h,w) we convert it to (1,h,w)
    if len(input_imgs.shape) == 2:
        input_imgs = np.expand_dims(input_imgs, 0)

    # input model size is (640,960) so imgs should be resize
    resize_imgs = []
    for img in input_imgs:
        img = cv2.resize(img, (960, 640))
        resize_imgs.append(img)

    inputs = np.array(resize_imgs, dtype=np.float32)

    # for deep model input shooud be (batch numbr, h,w,1)
    inputs = np.expand_dims(inputs, axis=-1)

    # normal imgs
    inputs = inputs/255.

    outs = model.predict(inputs)[0]
    # make predict model binary
    thresh = 0.3
    outs[outs >= thresh] = 1
    outs[outs < thresh] = 0

    # conver to opencv image format
    outs = outs * 255
    outs = outs.astype(np.uint8)
    outs = cv2.bitwise_not(outs)
    # cv2.imshow('mask',outs)
    # cv2.waitKey(0)

    # some morphology filter for better output
    outs = cv2.erode(outs, np.ones((3, 3)))
    outs = cv2.dilate(outs, np.ones((3, 3)))

    # resize to orginal
    outs = cv2.resize(outs, (1920, 1200))
    _, outs = cv2.threshold(outs, 50, 255, cv2.THRESH_BINARY)

    # finde contours
    cnts, h = cv2.findContours(outs, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    min_area = 5000
    max_area = 100000
    # filter by area and accept only white stone in mask
    res_cnts = list(filter(filter_stone(max_area, min_area, outs), cnts))

    # print(len(res_cnts))
    res_img = cv2.merge((input_imgs[0], input_imgs[0], input_imgs[0]))
    res_img = cv2.drawContours(res_img, res_cnts, -1, (0, 0, 255), 3)
    #cv2.imshow('res', res_img)
    # cv2.waitKey(0)

    stones_dict = {}
    info_dict = {}

    # make stone json
    for i, cnt in enumerate(res_cnts):
        x, y, w, h = cv2.boundingRect(cnt)  # calc contour bonding box

        stone_dict = {}
        stone_name = 'stone{}'.format(i+1)

        #stone_dict['contour'] = cnt.reshape((-1,2)).tolist()
        stone_dict['area'] = int(cv2.contourArea(cnt))
        stone_dict['length'] = h
        stone_dict['width'] = w
        stones_dict[stone_name] = stone_dict

    # make info json
    info_dict['count'] = len(res_cnts)

    # write Jsones

    # with open('info.json', 'w') as file:
    #     json.dump(info_dict,file)

    # with open('stones.json', 'w') as file:
    #     json.dump(stones_dict,file)

    return stones_dict, info_dict, res_img


def check_permission():
    try:
        f = open('permission.json')
        data = json.load(f)
        return data['permission']
    except:
        return False


imgs_path = 'images'
stones_json_path = 'stones'
info_json_path = 'informations'
res_img_path = 'results'
if __name__ == '__main__':
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    model = load_model()
    model.predict(np.random.rand(1, 640, 960, 1))
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    nfiles = 0  # len( os.listdir(imgs_path) )
    
    # img = np.zeros((100,100), dtype = np.uint8)
    # img[:,:] = np.random.randint(0,255)
    # cv2.imwrite('000000.jpg', img)

    while True:
        if check_permission():
            try:
                files = os.listdir(imgs_path)
                if len(files) > nfiles:
                    time.sleep(0.01)
                    files.sort(reverse=True)
                    fname = str(len(files)) + '.jpg'

                    img = cv2.imread(os.path.join(imgs_path, fname), 0)

                    stones_dict, info_dict, res_img = stone_detection(img)
                    cv2.imwrite(os.path.join(res_img_path, fname), res_img)

                    jfname = fname[: fname.find('.')] + '.json'

                    # print(jfname
                    path = os.path.join(info_json_path, jfname)
                    with open(path, 'w') as file:
                        json.dump(info_dict, file)

                    path = os.path.join(stones_json_path, jfname)
                    with open(path, 'w') as file:
                        json.dump(stones_dict, file)

                    nfiles = len(files)

                if len(files) == 0:
                    nfiles = 0
            except:
                continue

        else:
            nfiles = 0
            print('not')
            time.sleep(0.05)
