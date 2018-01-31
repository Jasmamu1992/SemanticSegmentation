import cv2, numpy, os
from PIL import Image
from glob import glob

images = sorted(glob('./runs/1517282896.278364/*.png')) # add path of the location of images
sampleImage = Image.open(images[0])
height, width = sampleImage.size

video = cv2.VideoWriter("SemanticSegmentation.avi", cv2.VideoWriter_fourcc(*'MJPG'), 10, (height, width))

for image in images:
    imagedata = Image.open(image)
    video.write(cv2.cvtColor(numpy.array(imagedata), cv2.COLOR_RGB2BGR))

video.release()