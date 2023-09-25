import requests
from bs4 import BeautifulSoup
import pyperclip

pasteurls=pyperclip.paste()
url_array=pasteurls.splitlines()

tag_name=input("Tag name:")

    # Create a text file to save the links
with open('linksText.txt', 'w') as file:
    for url in url_array:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')    
            for tag in soup.find_all(tag_name):
                print(tag.text)        
                file.write(tag.text + '\n')
        else:
            print('Failed to retrieve the web page.')



input()