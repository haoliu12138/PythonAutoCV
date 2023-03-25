import pyautogui as auto
import cv2 as cv
import os
import sys
# 切换工作目录到Photos下所有截图都会保存到这里 
print(f'当前工作目录为:{os.getcwd()}')
print('切换工作目录')
os.chdir(os.path.join(os.getcwd(),r'win32Gui\Photos'))
print(f'新工作目录为:{os.getcwd()}')
# 模板匹配的图标用来定位窗口
icon=cv.imread('PokeMmoIcon.png',cv.IMREAD_GRAYSCALE)
h,w=icon.shape
# 定位pokemmo窗口函数
def click_win():
    # 首先获取PokeMMO的窗口 并且截图
    try: 
        auto.screenshot('wholeWin.png')
    except Exception as err:
        print('截图时出现错误:',err)
        sys.exit(0)
    # 读取桌面截图
    try:
        win=cv.imread('wholeWin.png',cv.IMREAD_GRAYSCALE)
    except Exception as err:
        print('读取截图失败：',err)
        sys.exit(0)
    # 调用模板匹配获取坐标
    res=cv.matchTemplate(win,icon,cv.TM_CCOEFF)
    minval,maxval,minloc,maxloc=cv.minMaxLoc(res)
    # 左上角坐标
    top_left=maxloc
    # 右下角坐标
    button_right=(top_left[0]+w,top_left[1]+h)
    # 把范围画在上面做结果输出
    cv.rectangle(win,top_left,button_right,0,thickness=2)
    cv.imwrite('winres.png',win)
    # 点击图标使当前窗口定位到pokemmo
    auto.click(top_left[0]+w//2,top_left[1]+h//2)
# 定义刷经验操作函数
def expOperate():
    # 使用甜甜香气 根据你自己的快捷键设置
    auto.keyDown('3')
    auto.keyUp('3')
    # 使用技能
    auto.sleep(15)
    for i in range(3):
        auto.keyDown('z')
        auto.keyUp('z')

click_win()
for i in range(1):
    expOperate()
    auto.sleep(15)
 
    