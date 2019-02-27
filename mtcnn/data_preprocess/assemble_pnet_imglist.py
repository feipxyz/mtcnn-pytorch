import os
import sys
sys.path.append(os.getcwd())
import mtcnn.data_preprocess.assemble as assemble

# 项目基目录
base_path = os.path.join(os.getcwd(), '../..')

pnet_postive_file = os.path.join(base_path, './anno_store/pos_12.txt')
pnet_part_file = os.path.join(base_path, './anno_store/part_12.txt')
pnet_neg_file = os.path.join(base_path, './anno_store/neg_12.txt')
pnet_landmark_file = os.path.join(base_path, './anno_store/landmark_12.txt')
imglist_filename = os.path.join(base_path, './anno_store/imglist_anno_12.txt')

if __name__ == '__main__':

    anno_list = []

    anno_list.append(pnet_postive_file)
    anno_list.append(pnet_part_file)
    anno_list.append(pnet_neg_file)
    # anno_list.append(pnet_landmark_file)

    chose_count = assemble.assemble_data(imglist_filename ,anno_list)
    print("PNet train annotation result file path:%s" % imglist_filename)
