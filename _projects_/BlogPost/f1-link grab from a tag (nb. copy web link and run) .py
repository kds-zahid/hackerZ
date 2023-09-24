import requests
from bs4 import BeautifulSoup
import pyperclip

url=pyperclip.paste()

response = requests.get(url)



# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all "a" tags on the page
    a_tags = soup.find_all('a')
    
    # Create a text file to save the links
    with open('links.txt', 'w') as file:
        # Extract and write the links from the "href" attribute of each "a" tag to the text file
        for a_tag in a_tags:
            link = a_tag.get('href')
            if link is not None:
                file.write(link + '\n')
else:
    print('Failed to retrieve the web page.')