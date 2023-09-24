import tkinter as tk
import random
import tkinter.messagebox as msg
import pandas as pd
import time
import ctypes
import pyautogui
import pyperclip
from urllib.parse import urlparse


# https://docs.google.com/spreadsheets/d/1ZUvSpNw9r1FlqhnUtNhNrXzqTH_hnQqOvMHDeTJ7jhg/edit?usp=sharing
google_sheets_url = 'https://docs.google.com/spreadsheets/d/1ZUvSpNw9r1FlqhnUtNhNrXzqTH_hnQqOvMHDeTJ7jhg/edit'  # Replace with your spreadsheet URL

#image backlink
dfimgbacklink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=final_key'))
imgbacklinkarray = dfimgbacklink['keyword'].tolist()

# List of keyword names
keywordsarray = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon", "Mango", "Orange",
               "Peach", "Pear", "Pineapple", "Plum", "Raspberry", "Strawberry", "Watermelon", "Blueberry", "Papaya", "Coconut"]
keywordsarray=imgbacklinkarray
# Create a function to be called when the "Previous" button is clicked
def previous_click():
    current_index = scale.get()
    if current_index > 0:
        current_index -= 1
        scale.set(current_index)
        update_label(current_index)

# Create a function to be called when the "Next" button is clicked
def next_click():
    current_index = scale.get()
    if current_index < len(keywordsarray) - 1:
        current_index += 1
        scale.set(current_index)
        update_label(current_index)

# Create a function to be called when the slider value changes
def slider_changed(event):
    current_index = scale.get()
    update_label(current_index)

# Create a function to update the label
def update_label(index):
    if 0 <= index < len(keywordsarray):
        global current_keyword
        current_keyword = keywordsarray[index]
        label.config(text="Selected keyword: >> " + current_keyword)
        
    else:
        label.config(text="Invalid Index")

def h1button_c():
    pyperclip.copy(current_keyword)
    #pyperclip.copy(h1button.cget("text"))

# Create a Tkinter window
window = tk.Tk()
window.geometry("300x200")
# Create a "Previous" button widget
previous_button = tk.Button(window, text="<<", command=previous_click)

# Create a "Next" button widget
next_button = tk.Button(window, text=">>", command=next_click)

# Create a slider widget
scale = tk.Scale(window, from_=0, to=len(keywordsarray) - 1, orient="horizontal", label="keyword Index")

# Create a label widget to display the keyword name
label = tk.Label(window, text="Selected keyword: ")

h1button=tk.Button(window, text="h1 btn" , command=h1button_c)


# Pack the buttons, slider, and label into the window
previous_button.pack()
scale.pack()
next_button.pack()
label.pack()
h1button.pack()

# Bind the slider change event to the function
scale.bind("<Motion>", slider_changed)

# Start the Tkinter main loop
window.mainloop()