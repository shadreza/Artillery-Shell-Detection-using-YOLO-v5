import cv2
import numpy as np
import glob

size = ()

img_array = []
for filename in glob.glob("E:/Python/yolov5/yolov5/videos/b_slowmo_path1.avi"):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
