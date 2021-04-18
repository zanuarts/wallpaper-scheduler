import ctypes
import time
import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Wallpaper Scheduler", "The process has been started", duration=15)
os.chdir("F:\Python\wallpaper-scheduler")

img1 = r"F:\Python\wallpaper-scheduler\img\1.jpg"
img2 = r"F:\Python\wallpaper-scheduler\img\2.jpg"
img3 = r"F:\Python\wallpaper-scheduler\img\3.jpg"
img4 = r"F:\Python\wallpaper-scheduler\img\4.jpg"
img5 = r"F:\Python\wallpaper-scheduler\img\5.jpg"
img6 = r"F:\Python\wallpaper-scheduler\img\6.jpg"

def get_time():
    time.sleep(1)
    now = time.strftime("%H:%M:%S")
    return now

while True:
    time_change = str(get_time())
    if time_change == "05:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img1, 0)
    elif time_change == "08:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img2, 0)
    elif time_change == "10:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img3, 0)
    elif time_change == "12:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img4, 0)
    elif time_change == "16:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img5, 0)   
    elif time_change == "18:00:00":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img6, 0) 