# A Windows Automaton Wallpaper Scheduler 

Automaton helper to change your wallpaper in different time.

<hr>

## How to use

* Install requirements, simply run this command `python start.py`
* Config main.py and change the directory of the image
* Add wallpaperScheduler.vbs to your windows Registry Key by creating new String in this specific location: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
* Restart your computer, and your python script is now automatically running when startup

<hr>

## Notes

* You can change your wallpaper for free
* You can set your time freely
* If you difficult to config the .vbs file simply watch this [video](https://youtu.be/XWV9tatoPQI)
* If you have getting error in pywintypes, simply see this [topic](https://stackoverflow.com/questions/42482739/importerror-no-system-module-pywintypes-pywintypes34-dll/65539116#65539116)
* I don't take the responsibility if anything happen to your system
* Use `debug.py` to debug your code before saving it to `main.py`

<hr>

## Contribution

Freely to contribute to this project.
