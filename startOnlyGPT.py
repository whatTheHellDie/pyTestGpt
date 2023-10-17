from registerGPT import mRegisterGPT
import threading
from pynput import keyboard
import threading
 
isEnd = False
 
 
# 键盘按下执行的函数 使用try和except的原因是有特殊按键（功能键）
def keyboard_on_press(key):
    global isEnd
    try:
        key.char
    except AttributeError:
        
        if key == keyboard.Key.esc:
            print('退出键{0} press'.format(key)+",退出")
            isEnd = True
            return False
 
 
# 被中断的程序
def function():
    mRegisterGPT('user')
 
 
def main():
    global isEnd
    # 创建、启动键盘监听线程
    listener = keyboard.Listener(on_press=keyboard_on_press)
    listener.daemon = 1
 
    # 创建、启动鼠标监听线程
    t2 = threading.Thread(target=function)
    t2.daemon = 1
    listener.start()
    t2.start()
    while True:
        if isEnd:
            return
 
 
if __name__ == "__main__":
    main()

