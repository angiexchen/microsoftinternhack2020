from PIL import Image
import os 
import numpy as np
import cv2
from skimage.measure import compare_ssim

directory = './data2'

prev = None
gray_prev = None
hasPrev = False
count = 0 
maxCount = 0
for i in range(1, 888):
    maxCount += 1
    im = Image.open(directory + '/' + 'frame' + str(i) + '.jpg')
    current = np.array(im)
    gray_current = cv2.cvtColor(cv2.imread(directory + '/' + 'frame' + str(i) + '.jpg'), cv2.COLOR_BGR2GRAY)
    if (hasPrev):
        num = np.linalg.norm(current-prev)
        score = compare_ssim(gray_current, gray_prev)
        if score < 0.97:
            print(directory + '/' + 'frame' + str(i) + '.jpg')
            count += 1
    hasPrev = True
    prev = current  
    gray_prev = gray_current
print(count)
'''
gray_current1 = cv2.cvtColor(cv2.imread(directory + '/' + 'frame3564.jpg'), cv2.COLOR_BGR2GRAY)
gray_current2 = cv2.cvtColor(cv2.imread(directory + '/' + 'frame3565.jpg'), cv2.COLOR_BGR2GRAY)
print(compare_ssim(gray_current1, gray_current2))'''

'''im = np.array(im)
im2 = Image.open(directory + '/frame832.jpg')
im2 = np.array(im2)
num = np.linalg.norm(im - im2)
solve = im - im2
im = Image.fromarray(solve)
im.save('diff.jpg')
print(num)
'''