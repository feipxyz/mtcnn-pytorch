"""
RNet训练数据的anno中把路径写成了data_set，需要改成data
"""

import os
import re

# 项目基目录
base_path = os.path.join(os.getcwd(), '..')

prefix_path = ''
traindata_store = os.path.join(base_path, './data/train')

file_1 = os.path.join(base_path, './anno_store/neg_24.txt')
file_2 = os.path.join(base_path, './anno_store/pos_24.txt')
file_3 = os.path.join(base_path, './anno_store/part_24.txt')

data_files = (file_1, file_2, file_3)

for file in data_files:
    with open(file, "r") as f1, open("%s.bak" % file, 'w') as f2:
        for line in f1:
            f2.write(re.sub('data_set', 'data', line))

    os.remove(file)
    os.rename("%s.bak" % file, file)



