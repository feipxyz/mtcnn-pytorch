import os
import sys
sys.path.append(os.getcwd())
from wider_loader import WIDER
import cv2
import time
import os.path

HOME = os.path.expanduser("~")
cur = os.getcwd()

image_path = os.path.join(os.path.dirname(os.getcwd()), 'data/face_detection/WIDER_train/images/')

"""
 modify .mat to .txt 
"""

#wider face original images path
image_path = os.path.join(os.path.dirname(os.getcwd()), 'data/face_detection/WIDER_train/images')

#matlab file path

file_label_path = os.path.join(os.path.dirname(os.getcwd()), 'data/face_detection/wider_face_split/wider_face_split/wider_face_train.mat')

#target file path
target_file = os.path.join(os.path.dirname(os.getcwd()), 'anno_store/anno_train.txt')


wider = WIDER(file_label_path, image_path)

line_count = 0
box_count = 0

print('start transforming....')
t = time.time()

with open(target_file, 'w+') as f:
    # press ctrl-C to stop the process
    for data in wider.next():
        line = []
        line.append(str(data.image_name))
        line_count += 1
        for i,box in enumerate(data.bboxes):
            box_count += 1
            for j,bvalue in enumerate(box):
                line.append(str(bvalue))

        line.append('\n')

        line_str = ' '.join(line)
        f.write(line_str)

st = time.time()-t
print('end transforming')

print('spend time:%d'%st)
print('total line(images):%d'%line_count)
print('total boxes(faces):%d'%box_count)
