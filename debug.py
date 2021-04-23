import ctypes
import time
import datetime
import pywintypes
import os
from win10toast import ToastNotifier

img1 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\1.jpg"
img2 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\2.jpg"
img3 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\3.jpg"
img4 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\4.jpg"
img5 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\5.jpg"
img6 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\6.jpg"

dusk = "05:00:00"
sunrise = "08:00:00"
afternoon = "11:00:00"
sunset = "14:00:00"
dawn = "17:00:00"
night = "20:00:00"

def get_time():
    time.sleep(1)
    now = time.strftime("%H:%M:%S")
    return now

toast = ToastNotifier()
toast.show_toast("Wallpaper Scheduler", "The process has been started", duration=15)

# os.chdir(r"C:\Users\Homestead\Documents\wallpaper-scheduler")

while True:
    time_change = get_time()
    if time_change >= dusk and time_change < sunrise :
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img1, 0)
    elif time_change >= sunrise and time_change < afternoon:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img2, 0)
    elif time_change >= afternoon and time_change < sunset:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img3, 0)
    elif time_change >= sunset and time_change < dawn:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img4, 0)
    elif time_change >= dawn and time_change < night:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img5, 0)   
    elif time_change >= night and time_change < dusk:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img6, 0)
    else:
        print(time_change)