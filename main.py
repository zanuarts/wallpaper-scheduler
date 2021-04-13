import ctypes
import time

img1 = r"F:\Python\wallpaper-scheduler\img\1.jpg"
img2 = r"F:\Python\wallpaper-scheduler\img\2.jpg"
img3 = r"F:\Python\wallpaper-scheduler\img\3.jpg"
img4 = r"F:\Python\wallpaper-scheduler\img\4.jpg"
img5 = r"F:\Python\wallpaper-scheduler\img\5.jpg"
img6 = r"F:\Python\wallpaper-scheduler\img\6.jpg"

def get_time():
    time.sleep(1)
    time_now = time.strftime("%H:%M:%S")
    return time_now

while True:
    time_change = str(get_time())
    if time_change >= "05:00:00":
        print(time_change, "state 1")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img1, 0)
    elif time_change >= "08:00:00":
        print(time_change, "state 2")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img2, 0)
    elif time_change >= "10:00:00":
        print(time_change, "state 3")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img3, 0)
    elif time_change >= "12:00:00":
        print(time_change, "state 4")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img4, 0)
    elif time_change >= "16:00:00":
        print(time_change, "state 5")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img5, 0)   
    elif time_change >= "18:00:00":
        print(time_change, "state 6")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img6, 0) 
    else:
        print(time_change)