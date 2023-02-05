import os

classes = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
train_ann = 'D:\\Dataset\\flower_dataset\\train.txt'
val_ann = 'D:\\Dataset\\flower_dataset\\val.txt'
image_path = 'D:\\Dataset\\flower_dataset\\'
path = '/data/home/scv8939/run/mmclassification/data/flower/'


def writeTxt(imageList, txt_name, type, cls_name, cls_label):
    save_txt = open(txt_name, 'a')
    for img in imageList:
        save_txt.write(path + type + '/' + cls_name + '/' + img + " " + cls_label + '\n')


for i in range(len(classes)):
    train_dir = image_path + 'train\\'+classes[i]
    image_list = os.listdir(train_dir)
    writeTxt(image_list, train_ann, 'train', classes[i], str(i))

    val_dir = image_path + 'val\\' + classes[i]
    image_list = os.listdir(val_dir)
    writeTxt(image_list, val_ann, 'val', classes[i], str(i))

