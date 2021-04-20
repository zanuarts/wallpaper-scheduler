import ctypes
import time
import pywintypes
from win10toast import ToastNotifier

img1 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\1.jpg"
img2 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\2.jpg"
img3 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\3.jpg"
img4 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\4.jpg"
img5 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\5.jpg"
img6 = r"C:\Users\Homestead\Documents\wallpaper-scheduler\img\6.jpg"

def get_time():
    time.sleep(1)
    now = time.strftime("%H:%M:%S")
    return now

toast = ToastNotifier()
toast.show_toast("Wallpaper Scheduler", "The process has been started", duration=15)

# os.chdir(r"C:\Users\Homestead\Documents\wallpaper-scheduler")

while True:
    time_change = str(get_time())
    if time_change == "06:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img1, 0)
    elif time_change == "09:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img2, 0)
    elif time_change == "12:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img3, 0)
    elif time_change == "15:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img4, 0)
    elif time_change == "18:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img5, 0)   
    elif time_change == "21:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img6, 0)
    else:
        print(time_change)