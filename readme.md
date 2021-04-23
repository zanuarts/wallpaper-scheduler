# A Windows Automaton Wallpaper Scheduler 

Automaton helper to change your wallpaper in different time.

<hr>

## How to use

<ul>
    <li>Install requirements, simply run this command `python start.py`</li>
    <li>Config main.py and change the directory of the image</li>
    <li>Add wallpaperScheduler.vbs to your windows Registry Key by creating new String in this specific location: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`</li>
    <li>Restart your computer, and your python script is now automatically running when startup</li>
</ul>

<hr>

## Notes

<ul>
    <li>You can change your wallpaper for free</li>
    <li>You can set your time freely</li>
    <li>If you difficult to config the .vbs file simply watch this <a href="https://youtu.be/XWV9tatoPQI">video</a></li>
    <li>If you have getting error in pywintypes, simply see this <a href="https://stackoverflow.com/questions/42482739/importerror-no-system-module-pywintypes-pywintypes34-dll/65539116#65539116">topic</a></li>
    <li>I don't take the responsibility of anything happen</li>
    <li>Use debug.py to debug your code before saving it to main.py</li>
</ul>

<hr>

## Contribution

Freely to contribute to this project.