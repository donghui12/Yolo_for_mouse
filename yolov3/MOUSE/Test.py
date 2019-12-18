# import numpy as np
# import cv2

base_path = '/home/jdh/PyProject/yolo_for_mouse/yolov3/MOUSE/images/IMG_{}.JPG'

with open('train.txt', 'w', encoding='utf-8') as f:
    for i in range(3149, 3200):
        f.write(base_path.format(str(i))+'\n')

test_base_path = '/home/jdh/PyProject/yolo_for_mouse/yolov3/MOUSE/Valid/IMG_{}.JPG'

with open('test.txt', 'w', encoding='utf-8') as f:
    for i in range(3200, 3220):
        f.write(test_base_path.format(str(i))+'\n')
