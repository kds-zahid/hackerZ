import tkinter as tk
import pandas as pd
import random
import pyperclip




# https://docs.google.com/spreadsheets/d/1ZUvSpNw9r1FlqhnUtNhNrXzqTH_hnQqOvMHDeTJ7jhg/edit?usp=sharing
google_sheets_url = 'https://docs.google.com/spreadsheets/d/1ZUvSpNw9r1FlqhnUtNhNrXzqTH_hnQqOvMHDeTJ7jhg/edit'  # Replace with your spreadsheet URL

#image backlink
dfimgbacklink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=final_key'))
imgbacklinkarray = dfimgbacklink['keyword'].tolist()
fruitsarray=imgbacklinkarray

# Create the main window
window = tk.Tk()
window.title("GUI with Button and Label")
window.geometry("300x200")

# Variable to store text
abc = tk.StringVar()

# Function to handle button1 click event
def button1_click():
    aa=random.choice(imgbacklinkarray)
    abc.set(aa)

# Function to handle button1 click event
def button2_click():
    b2text=button2.cget("text")
    window.clipboard_clear()
    window.clipboard_append(b2text)

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
    if current_index < len(fruitsarray) - 1:
        current_index += 1
        scale.set(current_index)
        update_label(current_index)

# Create a function to be called when the slider value changes
def slider_changed(event):
    current_index = scale.get()
    update_label(current_index)

# Create a function to update the label
def update_label(index):
    if 0 <= index < len(fruitsarray):
        current_fruit = fruitsarray[index]
        label.config(text="Selected Fruit: " + current_fruit)
        pyperclip.copy(current_fruit)
    else:
        label.config(text="Invalid Index")



# Create a "Previous" button widget
previous_button = tk.Button(window, text="<<", command=previous_click)

# Create a "Next" button widget
next_button = tk.Button(window, text=">>", command=next_click)

# Create a slider widget
scale = tk.Scale(window, from_=0, to=len(fruitsarray) - 1, orient="horizontal", label="Fruit Index")

# Create a label widget to display the fruit name
label = tk.Label(window, text="Selected Fruit: ")

# Pack the buttons, slider, and label into the window
previous_button.pack()
scale.pack()
next_button.pack()
label.pack()

# Bind the slider change event to the function
scale.bind("<Motion>", slider_changed)

# Start the Tkinter main loop
window.mainloop()

# Create a button
button1 = tk.Button(window, text="Button 1", command=button1_click)

# Create a button
button2 = tk.Button(window, textvariable=abc, command=button2_click)

# Create a label to display the variable content
label = tk.Label(window, textvariable=abc)

# Pack the widgets
button1.pack()
# Pack the widgets
button2.pack()
label.pack()

# Start the main loop
window.mainloop()
