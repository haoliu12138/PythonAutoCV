import time
import cv2 as cv
import win32GuiUtil as util
import botOperation
import win32gui,win32ui,win32con
from windowsCapture import WindowCapture
def locate_to(winname):
    hwnd=win32gui.FindWindow(None,winname)
    # 这里直接定位到指定窗口，就不用获取这个调用sendmessage了，反正你点其他窗口也会中断操作
    # win=win32ui.CreateWindowFromHandle(hwnd)
    # 给某个窗口焦点
    win32gui.SetForegroundWindow(hwnd)
util.list_window_names()    
win32gui.SetForegroundWindow(134228)

wincap=WindowCapture(134228)

while True:
    img=wincap.getScerrnShot()
    cv.imshow('img',img)
    cv.waitKey(1)
botOperation.move(botOperation.Direction.right,7) 

# botOperation.move(botOperation.Direction.up,1) 

