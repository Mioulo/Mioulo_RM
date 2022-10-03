import os
# 图片所在路径
root_path = "D:\\Pyworkprojects\\yolov5-5.0\\VOCdevkit\\VOC2007\\JPEGImages"
filename_list = os.listdir(root_path)
number = 0
for filename in filename_list:
    if filename.endswith('.jpg'):
        src_img_path = os.path.join(os.path.abspath(root_path), filename)
        # new_img_code = filename.split('_')[1].split('.')[0].zfill(5)
        str_num=str(number)
        dst_img_path = os.path.join(os.path.abspath(root_path), str_num + '.jpg')
        number = number+1

        try:
            os.rename(src_img_path, dst_img_path)
            print('converting %s to %s ...' % (src_img_path, dst_img_path))
        except:
            continue