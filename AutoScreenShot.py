# Project Name: Auto Screenshot
# Description: Take screenshot of screen when any change take place.
# Author: Mani (Infinyte7)
# Date: 26-10-2020
# License: MIT

from pyscreenshot import grab
from PIL import ImageChops

import os
import time
import subprocess, sys
from datetime import datetime

import tkinter as tk
from tkinter import *
from tkinter import font

import imgcompare

class AutoScreenshot:
    def __init__(self, master):
        self.root = root
        
        root.title('Auto Screenshot')
        root.config(bg="white")

        fontRoboto = font.Font(family='Roboto', size=16, weight='bold')

        # project name label     
        projectTitleLabel = Label(root, text="Auto Screenshot v1.0.0")
        projectTitleLabel.config(font=fontRoboto, bg="white", fg="#5599ff")
        projectTitleLabel.pack(padx="10")

        # select monitoring area button
        btn_monitor_area = Button(root, text="Select Area to Monitor", command=self.select_monitor_area)
        btn_monitor_area.config(highlightthickness=0, bd=0, fg="white", bg="#4CAF50",
                                activebackground="#ffde21", activeforeground="white", font=fontRoboto)
        btn_monitor_area.pack(padx="10", fill=BOTH)

        # start button
        btn_start = Button(root, text="Start", command=self.start)
        btn_start.config(highlightthickness=0, bd=0, fg="white", bg="#5fd38d",
                         activebackground="#5fd38d", activeforeground="white", font=fontRoboto)
        btn_start.pack(padx="10", pady="10", fill=BOTH)

        # close button
        btn_start = Button(root, text="Close", command=self.close)
        btn_start.config(highlightthickness=0, bd=0, fg="white", bg="#f44336",
                         activebackground="#ff7043", activeforeground="white", font=fontRoboto)
        btn_start.pack(padx="10", pady="20", fill=BOTH)       

        # Placeholder for monitoring coordinates
        self.monitor_cords = None

    def start(self):
        # Create folder to store images
        directory = "Screenshots"
        self.new_folder = directory + "/" + datetime.now().strftime("%Y_%m_%d-%I_%M_%p")

        # all images to one folder
        if not os.path.exists(directory):
            os.makedirs(directory)

        # new folder for storing images for current session
        if not os.path.exists(self.new_folder):
            os.makedirs(self.new_folder)

        # Run ScreenCords.py and get cordinates
        cords_point = subprocess.check_output([sys.executable, "GetScreenCoordinates.py", "-l"])
        cord_tuple = tuple(cords_point.decode("utf-8").rstrip().split(","))

        # cordinates for screenshots and compare
        self.cords = (int(cord_tuple[0]), int(cord_tuple[1]), int(cord_tuple[2]), int(cord_tuple[3]))

        # save first image
        img1 = grab(bbox=self.cords)
        now = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        fname = self.new_folder + "/ScreenShots" + now + ".png"
        img1.save(fname)
        print("First Screenshot taken")

        # maintain a reference image for the selected monitoring area, if chosen
        if self.monitor_cords:
            self.ref_img = grab(bbox=self.monitor_cords)  # Capture monitoring area
        else:
            self.ref_img = img1  # Default to using the screenshot area if no monitor area is selected

        # start taking screenshots
        self.take_screenshots()       

    def select_monitor_area(self):
        # Run ScreenCords.py and get coordinates for the monitoring area
        cords_point = subprocess.check_output([sys.executable, "GetScreenCoordinates.py", "-l"])
        cord_tuple = tuple(cords_point.decode("utf-8").rstrip().split(","))

        # Store the monitoring coordinates
        self.monitor_cords = (int(cord_tuple[0]), int(cord_tuple[1]), int(cord_tuple[2]), int(cord_tuple[3]))
        print(f"Monitoring area set to: {self.monitor_cords}")

    def take_screenshots(self):
        # imgcompare param
        tolerance = 5

        # grab the current screenshot
        time.sleep(1)  # check screen every x seconds
        img2 = grab(bbox=self.cords)

        # grab the current state of the monitoring area
        if self.monitor_cords:
            monitor_img = grab(bbox=self.monitor_cords)  # use the selected monitoring area
        else:
            monitor_img = img2  # default to screenshot area if no monitor area selected

        # check difference between reference image and monitoring area image
        img_is_equal = imgcompare.is_equal(self.ref_img, monitor_img, tolerance)

        if not img_is_equal:
            now = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
            fname = self.new_folder + "/ScreenShots" + now + ".png"
            
            img2.save(fname)
            print("Screenshot taken")

            # Update reference image for next comparison
            self.ref_img = monitor_img

        # Call again after 5 milliseconds
        root.after(5, self.take_screenshots)

    def close(self):
        quit()

if __name__ == "__main__":  
    root = Tk()
    gui = AutoScreenshot(root)
    root.mainloop()