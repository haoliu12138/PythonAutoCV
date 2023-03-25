import ctypes.wintypes
import numpy as np
import win32gui,win32ui,win32con
class WindowCapture:
    # 截取宽高
    w=0
    h=0
    hwnd=None
    # 裁剪
    cropped_x=0
    cropped_y=0
    # 裁剪完和真实屏幕的偏移
    offect_x=0
    offect_y=0
    
    # 构造函数
    def __init__(self,window_name):
        self.hwnd=win32gui.FindWindow(None,window_name)
        if not self.hwnd:
            raise Exception('Window  not found:{}'.format(window_name))
        else:
            print('窗口句柄为{}'.format(self.hwnd))
        # 获取窗口大小
        # 改变以解决窗口大小变小
        # 解决地址 https://stackoverflow.com/questions/3192232/getwindowrect-too-small-on-windows-7
        try:
            f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        except WindowsError:
            raise Exception('size get error:{}'.format(window_name))
        if f:
            rect = ctypes.wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            f(ctypes.wintypes.HWND(self.hwnd),
            ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
            ctypes.byref(rect),
            ctypes.sizeof(rect)
            )
            self.w=rect.right - rect.left
            self.h=rect.bottom - rect.top       
            print(self.h,self.w)
        
        # border_pixels=8
        # titlebar_pixels=30
        
        # self.w=self.w-(border_pixels*2)
        # self.h=self.h-titlebar_pixels-border_pixels
        
        # self.cropped_x=border_pixels
        # self.cropped_y=titlebar_pixels
        
        # self.offect_x=windows_rect[0]+self.cropped_x
        # self.offect_x=windows_rect[1]+self.cropped_y
    # 构造函数
    def __init__(self,hwnd):
        self.hwnd=hwnd
        if not self.hwnd:
            raise Exception('Window  not found:{}'.format(hwnd))
        else:
            print('窗口句柄为{}'.format(self.hwnd))
        # 获取窗口大小
        # 改变以解决窗口大小变小
        # 解决地址 https://stackoverflow.com/questions/3192232/getwindowrect-too-small-on-windows-7
        try:
            f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        except WindowsError:
            raise Exception('size get error:{}'.format(hwnd))
        if f:
            rect = ctypes.wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            f(ctypes.wintypes.HWND(self.hwnd),
            ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
            ctypes.byref(rect),
            ctypes.sizeof(rect)
            )
            self.w=rect.right - rect.left
            self.h=rect.bottom - rect.top       
            print(self.h,self.w)
    # 获取截图
    def getScerrnShot(self):
        #获取窗口图像数据
        wDC=win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap=win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj,self.w,self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w,self.h),dcObj,(0,0),win32con.SRCCOPY)
        
        # 保存屏幕截图
        # dataBitMap.SaveBitmapFile(cDC,'debug.bmp')
        # 返回图片的获取
        sigenedIntsArray=dataBitMap.GetBitmapBits(True)
        img=np.fromstring(sigenedIntsArray,dtype='uint8')
        img.shape=(self.h,self.w,4)
        
        # 释放资源
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd,wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle()) 
        
        # 删除图片的alpha通道 否则模板匹配的时候会报错
        img=img[...,:3]
        
        img=np.ascontiguousarray(img)
        
        return img

    # 
    def get_screen_position(self,pos):
        return pos[0]+self.offect_x,pos[1]+self.offect_y


