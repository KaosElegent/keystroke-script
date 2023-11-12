'''
Created on July 1, 2023

@author: Shrey
'''
import pyautogui
import keyboard
import time
from tkinter import filedialog

txtPath = filedialog.askopenfilename(initialdir=".")

def code():
    with open(txtPath, 'r') as file:
        fileLines = file.readlines()
        time.sleep(0.5)
        for line in fileLines:
            pyautogui.write(line)

def listener():
    while True:     
        if keyboard.is_pressed('ctrl+f1'):
            time.sleep(3)
            code()
        elif keyboard.is_pressed('ctrl+f2'):
            return

if __name__=="__main__":
    listener()