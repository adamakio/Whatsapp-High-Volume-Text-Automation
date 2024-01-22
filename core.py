import os
import sys
import time
import pathlib
import requests
from platform import system
from exceptions import InternetException
from pyautogui import (
    write,
    click,
    hotkey,
    locateOnScreen,
    moveTo,
    press,
    size,
    typewrite,
)

WIDTH, HEIGHT = size()


def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""

    return "+" in number or "_" in number


def type_message(message: str) -> None:
    """Type message when cursor is on textbox"""

    if "///" in message:
        paragraphs = message.split("///")
        for paragraph in paragraphs:
            write(paragraph, interval=0.05)
            hotkey("shift", "enter")
    else:
        write(message, interval=0.05)


def press_enter() -> None:
    press("enter")


def copy_paste_image(img_path: str) -> None:
    """Copy and paste image from img_path"""

    copy_image(img_path)
    paste()


def copy_image(path: str) -> None:
    """Copy the Image to Clipboard based on the Platform"""

    if system().lower() == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    elif system().lower() == "windows":
        from io import BytesIO

        import win32clipboard
        from PIL import Image

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif system().lower() == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(
                f"osascript -e 'set the clipboard to (read (POSIX file \"{path}\") as JPEG picture)'"
            )
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    else:
        raise Exception(f"Unsupported System: {system().lower()}")


def paste() -> None:
    """Sends the Image to a Contact or a Group based on the Receiver"""

    typewrite(" ")
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")


def click_send() -> None:
    """click on text box"""
    if getattr(sys, "frozen", False):
        file = os.path.join(sys._MEIPASS, "files\send.png")
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = "files\send.png"
        file = os.path.join(dir_path, file_path)
    location = None
    while location is None:
        location = locateOnScreen(file, grayscale=True, confidence=0.5)
    moveTo(location.left + location.width / 2, location.top + location.height / 2)
    click()


def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    press("enter")
