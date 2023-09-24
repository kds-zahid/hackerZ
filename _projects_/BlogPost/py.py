import tkinter as tk

# Create a function to update the button label with the slider value
def update_button_label():
    value = slider.get()
    button.config(text=f"Slider Value: {value}")

# Create the main application window
root = tk.Tk()
root.title("Slider Example")

# Create a button
button = tk.Button(root, text="Slider Value: 0", command=update_button_label)
button.pack(pady=10)

# Create a slider
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_button_label)
slider.pack()

# Run the Tkinter main loop
root.mainloop()
