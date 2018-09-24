import numpy as np
from PIL import Image

def grayscale(file, n=32, m=32, color_number=4):
    im = Image.open(file)
    imgray = im.convert('L', palette=Image.ADAPTIVE)
    #reduse number of colours
    imgray = imgray.quantize(colors=color_number, method=None, kmeans=3, palette=None)#
    #resize image
    size = n,m
    imgray = imgray.resize(size,Image.NEAREST)
    return imgray

def grayscale_array(imgray, n=32, m=32, color_number=4):
    #create numerical array fron the picture
    img_array = np.array(list(imgray.getdata(band=0)), float)
    img_array.shape = (imgray.size[1], imgray.size[0])
    return img_array
    
if __name__ == "__main__":
    import sys
    imgray = grayscale(sys.argv[1])
    img_array = grayscale_array(sys.argv[1])
    print(sys.argv[1], img_array)