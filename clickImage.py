import webbrowser    
import pyautogui
import time
def clickImage(path,confidence=0.9):
    # 定义等待时间
    wait_time = 10  # 等待的总时间（秒）


    start_time = time.time()
    while True:
        # 尝试查找匹配的图片
        image_location = pyautogui.locateOnScreen(path, confidence = confidence)

        if image_location is not None:
            # 图片已经出现，执行相应的操作
            x, y = pyautogui.center(image_location)
        
            # 执行鼠标点击操作
            pyautogui.click(x, y)
            break
        # else:
        #     print("未找到指定图像"+path+",等待下个间隔寻找")

        # 检查是否超过等待时间
        elapsed_time = time.time() - start_time
        if elapsed_time >= wait_time:
            print("等待超时，未找到匹配的图片。"+path)
            break

        # 暂停一段时间再继续查找
        time.sleep(1)  # 休眠1秒后再继续查找
    # 如果找到图像
   