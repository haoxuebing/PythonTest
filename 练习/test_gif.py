from PIL import Image, ImageFont, ImageDraw
import argparse
import os
import imageio

# while 1:
file_name = './gifHandle/1.gif'
im = Image.open(file_name)
path = os.getcwd()
if (not os.path.exists(path + "/Cache")):
    os.mkdir(path + "/Cache")
os.chdir(path + "/Cache")
try:
    while 1:
        current = im.tell()
        name = '1.gif'.split('.')[0] + '-' + str(current) + '.png'
        size = (140*4,172*4)
        print(size)
        im2 =im.resize(size).convert('RGB')
        out = im2.resize(size,Image.ANTIALIAS)  
        out.save(name)
        #im.resize((300, 300), Image.ANTIALIAS)
        #im.save(name)# gif分割后保存的是索引颜色
        # print(name)
        im.seek(current + 1)
except:
    os.chdir(path)
    # im
