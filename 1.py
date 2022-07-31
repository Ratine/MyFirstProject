import pyperclip
import sys
import time
def copy(text):
    pyperclip.copy(text)
def openr():
    with open("D:/Clipboard/1.txt", "r") as f:
        return f.read()