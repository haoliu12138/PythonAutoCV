from operator import truediv
import win32gui
# win32gui工具类
# wine32Gui获取所有窗口句柄
def list_window_names():
    def winEnumHandler(hwnd,ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hwnd,'"'+win32gui.GetWindowText(hwnd)+'"')
    win32gui.EnumWindows(winEnumHandler,None)
#win32Gui获取窗口以及子窗口 返回一个窗口名及句柄字典
def get_inner_windows(whndl):
    def callback(hwnd,hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)]=hwnd
        return True
    hwnds={}
    win32gui.EnumChildWindows(whndl,callback,hwnds)
    return hwnds
