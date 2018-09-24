import numpy as np
from PIL import Image
from os import listdir

def grayscale(im, n=32, m=32, color_number=4):
    imgray = im.convert('L', palette=Image.ADAPTIVE)
    #reduse number of colours
    imgray = imgray.quantize(colors=color_number, method=None, kmeans=3, palette=None)#
    #resize image
    size = n,m
    imgray = imgray.resize(size,Image.NEAREST)
    #create numerical array fron the picture
    img_array = np.array(list(imgray.getdata(band=0)), float)
    img_array.shape = (imgray.size[1], imgray.size[0])
    return img_array, imgray
    
if __name__ == "__main__":
    import sys
    img_array, imgray = grayscale(sys.argv[1])
    print(sys.argv[1], img_array)