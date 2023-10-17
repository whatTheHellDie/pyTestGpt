import pyautogui

def clickMove(path,moveX=0,moveY=0):
        account_location = pyautogui.locateOnScreen(path)
        x, y = account_location.left, account_location.top

        # 下移15像素
        new_x = x +moveX
        new_y = y +moveY

        # 移动鼠标到新的位置
        pyautogui.moveTo(new_x, new_y)

        # 点击鼠标
        pyautogui.click()