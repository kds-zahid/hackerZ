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

#keyword 
dfimgbacklink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=final_key'))
keywordsarray = dfimgbacklink['keyword'].tolist()

# backlink
dfbacklink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=final_key'))
backlinkarray = dfimgbacklink['backlink'].tolist()

# Internal  keyword
dfInternalKeyword = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azInternalBacklink'))
InternalKeywordArray = dfInternalKeyword['internal_keyword'].tolist()
for internal_keyword_row in InternalKeywordArray:
    current_internal_keyword=internal_keyword_row

# Internal  keyword
dfinternal_backlink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azInternalBacklink'))
internal_backlinkArray = dfinternal_backlink['internal_backlink'].tolist()
for internal_backlink_row in internal_backlinkArray:
    current_internal_backlink=internal_backlink_row

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

#keyword backlink
dfimglink = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azimg'))
dfimglinkarray = dfimglink['imagelink'].tolist()
for imglinkarrayrow in dfimglinkarray:
    imglink=imglinkarrayrow

#paragraph lenth
dfparagraphlenth = pd.read_csv(google_sheets_url.replace('/edit', '/gviz/tq?tqx=out:csv&sheet=azuser'))
paragraphlentharray = dfparagraphlenth['pl'].tolist()
for paragraphlenthrow in paragraphlentharray:
    paragraph_lenght=paragraphlenthrow


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
        global current_backlink
        current_backlink = backlinkarray[index]
        label0.config(text= current_keyword)
        
    else:
        label.config(text="Invalid Index")

def h1button_c():
    pyperclip.copy(current_keyword)
    #pyperclip.copy(h1button.cget("text"))

def h2button_c():
    pyperclip.copy(current_backlink)
    #pyperclip.copy(h1button.cget("text"))



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
    paragraph41=[]
    paragraph42=[]

    # keyword backlink
    keywordbacklink="<a href='"+current_backlink+"'>"+current_keyword+"</a>"
    imgbacklink=imglink
    imgbacklink='<a href="'+current_backlink+'"><img class="alignnone size-medium wp-image-20935" src="'+imglink+'" alt="phone number list" width="300" height="197" /></a>'
    # internal keyword backlink
    internalKeywordBacklink="<a href='"+current_internal_backlink+"'>"+current_internal_keyword+"</a>"


    # Number of sentences
    num_sentences_in_paragraph = paragraph_lenght
    num_sentences_in_paragraphhalf = num_sentences_in_paragraph / 2
    
    # first paragraph
    while len(paragraph1)<num_sentences_in_paragraph:
        paragraph1.append(random.choice(textarray))
    
    # Join the selected sentences into a single paragraph
    paragraph_text1 = ' '.join(paragraph1)
    paragraphs.append(paragraph_text1)

    # second paragraphs>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    tittleh2="<h2>"+random.choice(tittlearray)+"</h2>"
    # Join the selected sentences into a single paragraph
    paragraphs.append(tittleh2)

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

    

    # third paragraph
    
    tittleh3="<h3>"+random.choice(tittlearray)+"</h3>"
    # Join the selected sentences into a single paragraph    
    paragraphs.append(tittleh3)

    # third paragraph img
    # Join the selected sentences into a single paragraph
    h3imgbacklink = imgbacklink
    paragraphs.append(h3imgbacklink)

    while len(paragraph3)<num_sentences_in_paragraph:
        paragraph3.append(random.choice(textarray))
    
    # Join the selected sentences into a single paragraph
    paragraph_text3 = ' '.join(paragraph3)
    paragraphs.append(paragraph_text3)



    # Fourth paragraphs>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    tittleh4="<h4>"+random.choice(tittlearray)+"</h4>"
    # Join the selected sentences into a single paragraph    
    paragraphs.append(tittleh4) 


    # fourth paragraph 1st
    while len(paragraph41)<num_sentences_in_paragraphhalf:
        paragraph41.append(random.choice(textarray))    
    # Join the selected sentences into a single paragraph
    paragraph_text4th1st = ' '.join(paragraph41)
    
    # second paragraph keyword backlink__________<<<<<<<<
    # Join the selected sentences into a single paragraph
    finalInternalkeywordbacklink = "假設您根據電子商務 "+internalKeywordBacklink+" 客戶的地理位置看到了"

    # second paragraph 2nd
    while len(paragraph42)<num_sentences_in_paragraphhalf:
        paragraph42.append(random.choice(textarray))    
    # Join the selected sentences into a single paragraph
    paragraph_text4th2nd = ' '.join(paragraph42)

    # final 2nd paragraph 
    fourth_paragraph_text=paragraph_text4th1st + finalInternalkeywordbacklink + paragraph_text4th2nd
    paragraphs.append(fourth_paragraph_text)

    # second paragraphs>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



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



# Create a Tkinter root
root = tk.Tk()
root.geometry("800x800")

# frame 0
frame=tk.Frame(root, bg="black")
frame.pack( padx=100, pady=100, side="top",fill="both")


# Create a "Previous" button widget
previous_button = tk.Button(frame, text="<<", command=previous_click)

# Create a "Next" button widget
next_button = tk.Button(frame, text=">>", command=next_click)

# Create a slider widget
scale = tk.Scale(frame, from_=0, to=len(keywordsarray) - 1, orient="horizontal", label="keyword Index")

# Create a label widget to display the keyword name

label0 = tk.Label(frame, text="Selected keyword: ")

h1button=tk.Button(frame, text="Tittle" , command=h1button_c)

h2button=tk.Button(frame, text="link" , command=h2button_c)


# Pack the buttons, slider, and label into the root
previous_button.pack(side='left')
scale.pack(side='left')
next_button.pack(side='left')
label0.pack(side='left')
h1button.pack(side='left')
h2button.pack(side='left')

# Bind the slider change event to the function
scale.bind("<Motion>", slider_changed)






# frame 1
frame1=tk.Frame(root, bg="black")
frame1.pack( padx=100, pady=100, side="top",fill="both")




# Create a button that calls the copy_tittle function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="Tittle", command=copy_tittle)
# Place the button on the window
button.pack(pady=3,side="left")

# Create a button that calls the username function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="text", command=copy_text)
# Place the button on the window
button.pack(pady=3,side='left')


# Create a button that calls the username function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="tag", )
# Place the button on the window
button.pack(pady=3,side='left')

# Create a button that calls the username function when clicked
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="category", )
# Place the button on the window
button.pack(pady=3,side='left')








# hide
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="hide", command=hide_text)
# Place the button on the window
button.pack(pady=3,side='left')

#...........................................................................................................
# close
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="x", command=close_app)
# Place the button on the window
button.pack(pady=3,side='left')

# minimize
button = tk.Button(frame1, bg="#252526", fg="white", highlightthickness=0,  width=10, text="-", command=minimize_app)
# Place the button on the window
button.pack(pady=3,side='left')
#...........................................................................................................

# frame 2
frame2=tk.Frame(root, bg="black")
frame2.pack(side="bottom",fill='x')

# Create a label widget with the text "Hello, world!"
label = tk.Label(frame2, bg="black", fg="white", justify="left", text="", wraplength=400)
# Place the label on the window
label.pack(side="left")




# Start the Tkinter main loop
root.mainloop()