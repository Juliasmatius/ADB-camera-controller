import os
import time
from config import *
def cmd(command):
    os.system(command)
def open_photo():
    print("Opened camera")
    cmd("adb shell am start -n "+activity_camera_name)
def open_video():
    print("Opened camera in video mode")
    cmd("adb shell am start -n "+activity_video_camera_name)
def exity():
    print("Exiting")
    cmd("adb kill-server")
    exit()
def take():
    print("Taking photo")
    cmd("adb shell input keyevent 27")
if is_remote:
    print("Please connect your phone with usb")
    cmd("pause")
    cmd("adb tcpip 5555")
    time.sleep(2)
    print("It is now ok to disconnect your device")
    cmd("pause")
    cmd("adb connect "+remote_ip)
else:
    cmd("adb start-server")
from nicegui import ui

ui.button('Take photo', on_click=lambda: take())
ui.button("Open camera app", on_click=lambda: open_photo())
ui.label("The one up there has no guarantee that it opens camera in photo mode")
ui.label("There for it's recomended that you check that it opened in camera mode")
ui.button("Open video", on_click=lambda: open_video())
ui.button("Exit", on_click=lambda: exity())
ui.run()