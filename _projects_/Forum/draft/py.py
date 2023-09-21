import pyautogui
import time
import pyperclip
from urllib.parse import urlparse

time.sleep(5)
pyautogui.hotkey("ctrl", "l")
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
forum_link=pyperclip.paste()
parse_forum_link=urlparse(forum_link)
forum_home=parse_forum_link.scheme + "://" + parse_forum_link.netloc
pyautogui.typewrite('hello world')
print(parse_forum_link)
print(forum_home)