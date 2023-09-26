import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

# Function to scrape and process the URL
def process_url():
    # Get the URL from the entry widget
    url = url_entry.get()
    
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Detect the encoding of the response
            encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
            
            # Parse the HTML content of the page with proper encoding
            soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)
            
            # Extract the text from the HTML
            text = soup.get_text()
            
            # Remove extra spaces and line breaks
            cleaned_text = ' '.join(text.split())  # Replaces multiple spaces with a single space
            cleaned_text = cleaned_text.replace('\n', ' ').replace('\r', '')  # Removes line breaks
            
            # Save the cleaned text to a text file
            with open('HackerZ_Article_text.txt', 'w', encoding='utf-8') as file:
                file.write(cleaned_text)
            
            #messagebox.showinfo('Success', 'Cleaned text saved to cleaned_text.txt')
        else:
            messagebox.showerror('Error', 'Failed to retrieve the webpage')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Function to close the window
def close_window():
    window.destroy()

# Function to clear the placeholder text when the user clicks on the entry box
def clear_placeholder(event):
    if url_entry.get() == "Enter URL":
        url_entry.delete(0, tk.END)
        url_entry.config(fg='black')  # Change text color to black

# Create a Tkinter window
window = tk.Tk()
window.title('HackerZ Article Grabber')
window.configure(bg='#121212') 

window.overrideredirect(True)  # Hide the title bar


# Create a label with a dark theme
label = tk.Label(window, text='HackerZ Article Grabber', bg='#121212', fg='white')
label.pack(fill=tk.BOTH, expand=True)  # Center both horizontally and vertically

# Create an entry widget for URL input with a dark theme and placeholder text
url_entry = tk.Entry(window, width=40, bg='#333333', fg='gray', insertbackground='white')
url_entry.insert(0, 'Enter URL')
url_entry.bind("<FocusIn>", clear_placeholder)  # Bind the function to clear the placeholder text
url_entry.pack(fill=tk.BOTH, expand=True)  # Center both horizontally and vertically


# Create a button with a dark theme
process_button = tk.Button(window, text='Grab', command=process_url, bg='#333333', fg='white')
process_button.pack(fill=tk.BOTH, expand=True)  # Center both horizontally and vertically

# Create a button with a dark theme to close the window
close_button = tk.Button(window, text='Close', command=close_window, bg='#333333', fg='white')
close_button.pack(fill=tk.BOTH, expand=True)  # Center both horizontally and vertically


# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - window.winfo_reqwidth()) // 2
y = (screen_height - window.winfo_reqheight()) // 2

# Set the window's position
window.geometry('+{}+{}'.format(x, y))

# Run the Tkinter event loop
window.mainloop()
