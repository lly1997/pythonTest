import pyautogui
import time
#   模拟鼠标 跳动

pyautogui.moveTo(400, 175 +  20,
    duration = 0.5)
pyautogui.click(clicks = 2, button =
    'left', interval = 0.05)# 点击进入单据
time.sleep(3)
pyautogui.click(100, 140)# 点击修改
time.sleep(3)
pyautogui.click(350, 190, button =
    'left')# 左击发货日
pyautogui.click(350, 190, button =
    'right')# 右击发货日
time.sleep(1.5)
pyautogui.click(595, 397)# 选择日期5
time.sleep(1.5)
pyautogui.click(815, 472)# 完成
time.sleep(1.5)
pyautogui.click(565, 425)# 发出日大于接收日， 是
time.sleep(1.5)
pyautogui.click(155, 140)# 点击保存
time.sleep(2)
pyautogui.click(432, 140)# 点击查询
time.sleep(5)