import os
import random
import shutil
import csv
import numpy as np


def CopyFile(imageDir, test_rate, save_test_dir, save_train_dir):
    image_number = len(imageDir)
    # 要移动的图片数目
    test_number = int(image_number * test_rate)
    print("要移动到%s目录下的图片数目为:%d" % (save_test_dir, test_number))
    # 随机截取列表imageDir中数目为test_number的元素
    test_samples = random.sample(imageDir, test_number)
    # copy图像到目标文件夹
    if not os.path.exists(save_test_dir):
        os.makedirs(save_test_dir)
        print("save_test_dir has been created successfully!")
    else:
        print("save_test_dir already exited!")
    if not os.path.exists(save_train_dir):
        os.makedirs(save_train_dir)
        print("save_train_dir has been created successfully!")
    else:
        print("save_train_dir already exited!")
    for i, j in enumerate(test_samples):
        shutil.copy(test_samples[i], save_test_dir+test_samples[i].split("\\")[-1])
    print("tets移动完成！")
    for train_imgs in imageDir:
        if train_imgs not in test_samples:
            shutil.copy(train_imgs, save_train_dir+train_imgs.split("\\")[-1])
    print("train移动完成")


file_path = r"D:\Dataset\flower_dataset\flower"
test_rate = 0.2

file_dirs = os.listdir(file_path)
origin_paths = []
save_train_dirs = []
save_val_dirs = []
for path in file_dirs:
   origin_paths.append(file_path+'\\'+path+"\\")
   save_train_dirs.append(file_path[:-6]+"train\\"+path+"\\")
   save_val_dirs.append(file_path[:-6]+"val\\"+path+"\\")
for i, origin_path in enumerate(origin_paths):
    # 获得原始路径下的所有图片的name（默认路径下都是图片）
    image_list = os.listdir(origin_path)
    image_Dir = []
    for x, y in enumerate(image_list):
        image_Dir.append(os.path.join(origin_path, y))
    print("%s目录下共有%d张图片！" % (origin_path, len(image_Dir)))
    CopyFile(image_Dir, test_rate, save_val_dirs[i], save_train_dirs[i])
print("all datas has been moved successfully!")

