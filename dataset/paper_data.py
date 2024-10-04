import os

# 设置基本路径

images_dir = 'images'
txt_dir = 'dataSet/Main'
output_dir = 'dataSet/paper_data'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历Main文件夹中的所有.txt文件
for txt_file in os.listdir(txt_dir):
    if txt_file.endswith('.txt'):
        # 读取当前txt文件的完整路径
        txt_path = os.path.join(txt_dir, txt_file)

        # 构造新txt文件的完整路径
        new_txt_path = os.path.join(output_dir, txt_file)

        # 读取原始txt文件的内容
        with open(txt_path, 'r') as file:
            image_ids = file.read().strip().split()

            # 写入新txt文件
        with open(new_txt_path, 'w') as new_file:
            for image_id in image_ids:
                # 构造图像的完整路径
                image_path = os.path.join(r'D:\tools\pycharm\project\datas\mydatas\images', f'{image_id}.png')
                # 写入新txt文件
                new_file.write(image_path + '\n')

print("处理完成！")
