# 第二步：导入PIL图片库

from PIL import Image

# 第三步：制作Gif动图

# （1）打开原始素材图片

im = Image.open(r"1.jpg")

# （2）将原始素材图片旋转30度存入列表

images = [ ]

images.append(im.rotate(10))
images.append(im.rotate(30))

# （3）将列表中的图片和原始图片合并保存

im.save(r"./cat.gif",

save_all=True,

append_images=images)