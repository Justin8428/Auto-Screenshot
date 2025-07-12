# Auto-Screenshot
Automatically take screenshots of part of screen, when there are differences or some changes in some region of the screen.

It is useful when you are watching an online live or pre-recorded lecture and need to take a screenshot of every slide in the lecture, and the ppt is not available. 

This version allows monitoring of only part of the screen, useful if e.g. the Zoom presenter is covering part of the powerpoint.

# How to use
0. Download the scripts -- click Code --> Download ZIP --> extract to a folder e.g. Desktop
1. Install Python
2. Install following python modules in terminal
```
pip install pyqt5 pyscreenshot pillow imgcompare
```
You can also install by running the following in terminal.
```
pip install -r requirements.txt
```
Note: Linux users may need to use `pip3` instead of `pip`, and also install `python3-tk` through their system package manager. e.g. Debian-based should run `sudo apt-get install python3-tk`
3. Open terminal, change directory to extracted folder, and run ```py AutoScreenshot.py``` via terminal
4. Click ```Select Area to Monitor``` and draw rectangular part on screen where you want to monitor changes.
4. Click ```Start``` and draw rectangular part on screen where you want to screenshot.
5. Now it will take screenshot when the monitoring area changes automatically. Images will be saved in a subfolder with the current date and time.
6. Close the program once finished.

# Notes

Image comparison algorithm uses the imgcompare library. The default tolerance value is set to 5.0, you can set it by editing the code.

# License
MIT License

All credits to Mani who was the original author of the program.

# TODO

 - EXE file
 - Better directions / readme
