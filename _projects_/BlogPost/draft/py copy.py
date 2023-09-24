import tkinter as tk
import pyperclip

# Create a function to update the button label with the slider value
def update_button_label():
    value = slider.get()
    button.config(text=f"Slider Value: {value}")

# Create a function to copy the button text to the clipboard
def copy_to_clipboard():
    text_to_copy = button.cget("text")
    pyperclip.copy(text_to_copy)

# Create the main application window
root = tk.Tk()
root.title("Slider Example")

# Create a button
button = tk.Button(root, text="Slider Value: 0", command=update_button_label)
button.pack(pady=10)

# Create a slider
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_button_label)
slider.pack()

# Create a button to copy the text to the clipboard
copy_button = tk.Button(root, text="Copy Text", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
