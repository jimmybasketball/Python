#!D:\Python\python27
# -*- coding:utf-8 -*-
__author__ = 'jimmy'
import os
import PIL,numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

need_update = True
# cor = [0,0]
# click_count = 0

def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')#获取当前界面的手机截图
    os.system('adb pull /sdcard/screen.png')#下载当前这个截图到当前电脑当前文件夹下
    print('执行图片提取')
    return numpy.array(PIL.Image.open('screen.png'))

def jump_to_next(point1, point2):#计算炫的长度
    x1, y1 = point1; x2, y2 = point2
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance*1.35)))
    print('执行计算玄长度')

def on_calck(event, coor=[]):#绑定的鼠标单击事件
    global need_update
    print('执行鼠标按钮')
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
    need_update = True

def update_screen(frame):#更新图片 /从画图片
    global need_update
    print('执行更新图片')
    if need_update:
        time.sleep(2)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,

fig = plt.figure()#创建一个空白的图片对象/创建一张图片
axes_image = plt.imshow(get_screen_image(), animated=True)#把获取的图片画在坐标轴上面
print('执行鼠标。。。。')
fig.canvas.mpl_connect('button_press_event', on_calck)
print('执行点击')
ani = FuncAnimation(fig, update_screen, interval=50, blit=True)
plt.show()
