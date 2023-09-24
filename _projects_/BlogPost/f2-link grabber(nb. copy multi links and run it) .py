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
        soup = BeautifulSoup(response.text, 'html.parser')    
        for tag in soup.find_all(tag_name):
            print(tag.text)        
            file.write(tag.text + '\n')
input()