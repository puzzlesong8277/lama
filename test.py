import os

def find_mask_without_name(input_dir):
# 存储符合条件的文件名
    missing_name_files = []

    # 获取目录中的所有文件
    for file_name in os.listdir(input_dir):
        # 判断文件名是否以 _mask.png 结尾
        if file_name.endswith('_mask.png'):
        # 获取对应的 name.png 文件名（去掉 _mask）
            base_name = file_name.replace('_mask.png', '.png')

            # 检查对应的 name.png 文件是否存在
            if not os.path.exists(os.path.join(input_dir, base_name)):
                missing_name_files.append(file_name)
                #os.remove(os.path.join(input_dir,file_name))

    return missing_name_files

    # 示例：指定文件夹目录
input_directory = 'mural/y_color_correction' # 替换为实际目录路径
missing_files = find_mask_without_name(input_directory)

    # 输出所有符合条件的文件
if missing_files:
    print("以下是存在 _mask.png 但缺少对应 .png 文件的图片：")
    for file in missing_files:
        print(file)
    else:
        print("没有找到任何缺少对应 .png 文件的 _mask.png 文件。")
    
