import webbrowser    
import pyautogui
import time
import random
import string
from clickImage import clickImage
from addDataXlsx import addDataXlsx
from registerGPT import mRegisterGPT
from clickMove import clickMove

import keyboard
def generate_random_string():
    # 生成前两位的随机大写字母
    upper_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    # 生成六位随机小写字母
    lower_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

    # 生成四位随机数字
    numbers = ''.join(random.choice(string.digits) for _ in range(4))

    upper_letters1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    # 组合生成的部分以生成最终的字符串
    final_string = upper_letters + lower_letters + numbers+upper_letters1

    return final_string

def generate_random_password():
    # 生成前两位的随机大写字母
    upper_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    # 生成六位随机小写字母
    lower_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

    # 生成两位随机数字
    numbers = ''.join(random.choice(string.digits) for _ in range(2))

    # 组合生成的部分以生成最终的字符串
    final_string = upper_letters + lower_letters + numbers

    return final_string


def registerProtonMail():
   while True:
    obj=setMailInfoAndCheckRepeat()
    print(obj)
    submit_location=obj['submit_location']

    if submit_location is not None:
        # 账号重复
        clickMove('images/2.png',-35,0)
    else:
        addDataXlsx('account',{"newAccount": obj['newAccount'], "newPassword": obj['newPassword']})
        keyboard.wait('ctrl+alt+l')
        print('pass')
        mRegisterGPT('auto')
        break
    



def setMailInfoAndCheckRepeat():
   # 调用方法生成随机邮箱名称字符串
   random_string = generate_random_string()
#    random_string = 'fffqbcd123@proton.me'
   random_password = generate_random_password()
   pyautogui.hotkey('ctrl', 'a')
   pyautogui.typewrite(random_string)
   pyautogui.press('tab')
   pyautogui.press('tab')
   pyautogui.typewrite(random_password)
   pyautogui.press('tab')
   pyautogui.typewrite(random_password)
   clickImage('images/3.png')
   time.sleep(3)  # 休眠5秒后再继续查找
   submit_location = pyautogui.locateOnScreen('images/3.png')
 
   return {"newAccount": random_string, "newPassword": random_password,"submit_location":submit_location}
