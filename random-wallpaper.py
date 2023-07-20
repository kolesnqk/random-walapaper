import random
import ctypes
import os

path = ''  # point to the path

def set_wallpaper(path):
    files = os.listdir(path) #get a list of files in the folder
    image = random.choice(files) #select a random file
    image_path = path + image
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)  #set the image as wallpaper

set_wallpaper(path)
