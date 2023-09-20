# Import the modules
import tkinter as tk
import random
import tkinter.messagebox as msg
import pandas as pd
import time
import ctypes

time.sleep(2)

abc="""
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀
⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀
⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀
⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀
⠀⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀
⠀⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


google_sheets_url = 'https://docs.google.com/spreadsheets/d/13IKBcN92SUDUdhqyzpQ8TW1PnQgOtHmVqZYbDGqVP4g/edit'  # Replace with your spreadsheet URL

#image backlink
dfimgbacklink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azuser'))
imgbacklinkarray = dfimgbacklink['imagebacklink'].tolist()
for imgrow in imgbacklinkarray:
        imgbacklink=imgrow

#keyword backlink
dfkeywordbacklink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azuser'))
keywordbacklinkarray = dfkeywordbacklink['keywordbacklink'].tolist()
for keywordbacklinkrow in keywordbacklinkarray:
    keywordbacklink=keywordbacklinkrow

# usename
dfusername = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azuser'))
usenamearray = dfusername['username'].tolist()

# password
dfpassword = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azuser'))
passwordarray = dfpassword['password'].tolist()

# email
dfemail = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azuser'))
emailarray = dfemail['email'].tolist()

# tittle
dftittle = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=aztittle'))
tittlearray = dftittle.values.tolist()
# convert to a single list
tittlearray = sum(tittlearray,[])

# text
dftext = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=aztext'))
textarray = dftext.values.tolist()
# convert to a single list
textarray=[item for sublist in textarray for item in sublist]

# Define username
def copy_username():
    # Copy the tittle name to the clipboard
    for row in usenamearray:
        username=row
    root.clipboard_clear()
    root.clipboard_append(username)
    # Display a message on the button
    label.config(text="Copied " + username)

# Define password
def copy_password():
    # Copy the tittle name to the clipboard
    for row in passwordarray:
        password=row
    root.clipboard_clear()
    root.clipboard_append(password)
    # Display a message on the label
    label.config(text="Copied " + password)

# Define password
def copy_email():
    # Copy the tittle name to the clipboard
    for row in emailarray:
        email=row
    root.clipboard_clear()
    root.clipboard_append(email)
    # Display a message on the label
    label.config(text="Copied " + email)

# Define the function that copies a random tittle name to the clipboard
def copy_tittle():
    # Choose a random tittle name from the list
    random_tittle = random.choice(tittlearray)
    # Copy the tittle name to the clipboard
    root.clipboard_clear()
    root.clipboard_append(random_tittle)
    # Display a message on the label
    label.config(text="Copied " + random_tittle)

# Define the function that copies a random tittle name to the clipboard
def copy_text():
    # initialize
    paragraphs = []
    paragraph1=[]
    paragraph21=[]
    paragraph22=[]
    paragraph3=[]
    # Number of sentences
    num_sentences_in_paragraph = 10
    num_sentences_in_paragraphhalf = num_sentences_in_paragraph / 2
    
    # first paragraph
    while len(paragraph1)<num_sentences_in_paragraph:
        paragraph1.append(random.choice(textarray))
    
    # Join the selected sentences into a single paragraph
    paragraph_text1 = ' '.join(paragraph1)
    paragraphs.append(paragraph_text1)

    # second paragraphs>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # second paragraph 1st
    while len(paragraph21)<num_sentences_in_paragraphhalf:
        paragraph21.append(random.choice(textarray))    
    # Join the selected sentences into a single paragraph
    paragraph_text2nd1st = ' '.join(paragraph21)
    
    # second paragraph keyword backlink__________<<<<<<<<
    # Join the selected sentences into a single paragraph
    finalkeywordbacklink = "假設您根據電子商務 "+keywordbacklink+" 客戶的地理位置看到了"

    # second paragraph 2nd
    while len(paragraph22)<num_sentences_in_paragraphhalf:
        paragraph22.append(random.choice(textarray))    
    # Join the selected sentences into a single paragraph
    paragraph_text2nd2nd = ' '.join(paragraph22)

    # final 2nd paragraph 
    paragraph_text=paragraph_text2nd1st + finalkeywordbacklink + paragraph_text2nd2nd
    paragraphs.append(paragraph_text)

    # second paragraphs>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # second paragraph img
    # Join the selected sentences into a single paragraph
    paragraph_text = imgbacklink
    paragraphs.append(paragraph_text)

    # third paragraph
    while len(paragraph3)<num_sentences_in_paragraph:
        paragraph3.append(random.choice(textarray))
    
    # Join the selected sentences into a single paragraph
    paragraph_text3 = ' '.join(paragraph3)
    paragraphs.append(paragraph_text3)


    # Join the paragraphs with newlines
    result = '\n\n'.join(paragraphs)

    #initialize
    random_text=result


    # Copy the tittle name to the clipboard
    root.clipboard_clear()
    root.clipboard_append(random_text)
    # Display a message on the label
    label.config(text="Copied " + random_text)


# Define the function that copies a random tittle name to the clipboard
def hide_text():
    label.config(text="")

# Function to close the application
def close_app():
    root.destroy()

# Function to close the application
def minimize_app():
    root.iconify()


# Create the root window
root = tk.Tk()
# Set the window title
root.title("HackerZ")
# Set the window size
root.geometry("300x200")
# Disable window resizing (maximizing and resizing)
#root.resizable(False, False)
# color 
root.configure(bg="black")
# Set the background color of the title bar to black
root.wm_attributes("-topmost", 5)  # This line makes the title bar visible on some systems
root.wm_attributes("-fullscreen", True)  # This line allows minimizing and maximizing the window
root.wm_attributes("-transparentcolor", "black")  # Set the transparent color to black


# frame 1
frame1=tk.Frame(root, bg="black")
frame1.pack( padx=100, pady=100, side="top",fill="both")

# Create a button that calls the copy_tittle function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="username", command=copy_username)
# Place the button on the window
button.pack(pady=3,side='left')

# Create a button that calls the copy_tittle function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="password", command=copy_password)
# Place the button on the window
button.pack(pady=3,side='left')

# Create a button that calls the copy_tittle function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="email", command=copy_email)
# Place the button on the window
button.pack(pady=3,side='left')

# frame mid
framemid=tk.Frame(root, bg="black")
framemid.pack(side="top",fill="y")

# Create a button that calls the copy_tittle function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="Tittle", command=copy_tittle)
# Place the button on the window
button.pack(pady=3,side="left")

# Create a button that calls the username function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="text", command=copy_text)
# Place the button on the window
button.pack(pady=3,side='left')

# hide
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="hide", command=hide_text)
# Place the button on the window
button.pack(pady=3,side='left')

# close
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="x", command=close_app)
# Place the button on the window
button.pack(pady=3,side='left')

# minimize
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="-", command=minimize_app)
# Place the button on the window
button.pack(pady=3,side='left')

# frame 2
frame2=tk.Frame(root, bg="black")
frame2.pack(side="bottom",fill='x')

# Create a label widget with the text "Hello, world!"
label = tk.Label(frame2, bg="black", fg="white", justify="left", text="", wraplength=400)
# Place the label on the window
label.pack(side="left")


# Start the main loop
root.mainloop()