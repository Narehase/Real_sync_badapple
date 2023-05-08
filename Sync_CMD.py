def gos(x = 0,y = 0):
    print(f"\033[{x};{y}H",end="")
    
def asia(line:list):
    hg = [" ", ".", ":", "/","?", ">","#","#"]
    a = ""
    for i in line:
        c = i[0]
        c = int(c/36.42857142857143)
        a+= hg[c]
    
    return a


import numpy as np
import cv2
import os
import time
# import pyautogui
# import keyboard

# def point_up():
#     points = []
#     key = 0
#     i = 0
#     print("point_UP! || 포인트순서 : 좌측상단 -> 우측하단")
#     while True:
#         if keyboard.is_pressed('space') and key == 0:
#             x,y = pyautogui.position()
#             print(i," : ",x)
#             points.append([x,y])
#             i += 1
#             key = 1

#         if key == 1:
#             key = 0
#             time.sleep(0.2)
#         if i == 2:
#             break

#     print(points)
#     return points

v = cv2.VideoCapture("bb.mp4")
_,f = v.read()
# cp = point_up()
# f = pyautogui.screenshot(region=(cp[0][0],cp[0][1],cp[1][0],cp[1][1]))
prev_time = 0
FPS = 29.97
c_FPS = 0
frames = True
for i in range(3):
    print(i)
    time.sleep(1)
# keyboard.press("space")
os.system("cls")
st = time.time()
while _:
    _,f = v.read()
    if not _:
        break
    # os.system("cls")
    gos()
    f = cv2.resize(f, (70,50))
    a = "\n"
    
    for i in f:        
        a += asia(i)+"\n"
    a += "\n"
    while frames:
        current_time = time.time()
        if current_time > st + (1./ FPS)*c_FPS:
            c_FPS += 1
            frames = False
            print(a)
    frames = True
