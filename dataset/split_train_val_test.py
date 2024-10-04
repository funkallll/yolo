# 自动划分数据集
# coding:utf-8

import os
import random
import argparse

parser = argparse.ArgumentParser()
# xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
parser.add_argument('--xml_path', default='xml', type=str, help='input xml labels path')
# 数据集的划分，地址选择自己数据下的ImageSets/Main
parser.add_argument('--txt_path', default='dataSet/Main', type=str, help='output txt labels path')
opt = parser.parse_args()

xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)

# 计算每个集合的大小
train_size = int(num * 0.8)
val_size = int(num * 0.1)
test_size = num - train_size - val_size  # 或者直接 int(num * 0.1)，因为比例总和为1

# 确保计算出的集合大小是整数且总和等于总文件数（处理浮点数计算误差）
assert train_size + val_size + test_size == num, "Calculated sizes do not sum up to total number of files."

# 打乱文件列表
random.shuffle(total_xml)

# 划分集合
train_files = total_xml[:train_size]
val_files = total_xml[train_size:train_size + val_size]
test_files = total_xml[train_size + val_size:]

# 保存文件
with open(txtsavepath + '/train.txt', 'w') as file_train, \
        open(txtsavepath + '/val.txt', 'w') as file_val, \
        open(txtsavepath + '/test.txt', 'w') as file_test:
    for file in train_files:
        name = file[:-4] + '\n'  # 假设文件名以.xml结尾，去掉扩展名
        file_train.write(name)

    for file in val_files:
        name = file[:-4] + '\n'
        file_val.write(name)

    for file in test_files:
        name = file[:-4] + '\n'
        file_test.write(name)

    # 注意：这里没有创建trainval.txt文件，因为题目要求的是train:val:test的比例划分。
# 如果确实需要trainval集合，可以简单地将train_files和val_files合并后写入trainval.txt。
