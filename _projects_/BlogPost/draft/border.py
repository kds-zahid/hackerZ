import tkinter as tk

def set_scale_color(event):
    canvas.itemconfig(scale_border, outline="red")

root = tk.Tk()
root.title("Scale Border Color Example")

# Create a Frame to contain the Scale widget
frame = tk.Frame(root)
frame.pack()

# Create a Canvas widget for the border
canvas = tk.Canvas(frame, width=500, height=30)
canvas.pack()

# Create a Scale widget within the Frame
scale = tk.Scale(frame, from_=0, to=100, orient="horizontal")
scale.pack()

# Create a border for the Scale using the Canvas widget
scale_border = canvas.create_rectangle(0, 0, 500, 30, outline="black", width=2)

# Bind an event to change the border color when Scale is clicked
scale.bind("<Button-1>", set_scale_color)

# Start the Tkinter main loop
root.mainloop()
