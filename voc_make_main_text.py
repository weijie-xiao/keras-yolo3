import os
import random

root_dir = r"F:\stagesepx\image_set_for_train\zhuiwan\show_yuyin"

trainval_percent = 0.66
train_percent = 0.5
xmlfilepath = os.path.join(root_dir, 'Annotations')
txtsavepath = os.path.join(root_dir, 'ImageSets', 'Main')
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open(os.path.join(txtsavepath, "trainval.txt"), 'w')
ftest = open(os.path.join(txtsavepath, "test.txt"), 'w')
ftrain = open(os.path.join(txtsavepath, "train.txt"), 'w')
fval = open(os.path.join(txtsavepath, "val.txt"), 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()