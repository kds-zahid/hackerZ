import requests
from bs4 import BeautifulSoup
import pyperclip

url=pyperclip.paste()

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all div elements with class "elementor-col-16"
    div_elements = soup.find_all('div', class_='elementor-col-16')
    
    # Loop through each div element
    for div_element in div_elements:
        # Find all "a" tags within the current div element
        a_tags = div_element.find_all('a')
        
        # Extract and print the links from the "href" attribute of each "a" tag
        for a_tag in a_tags:
            link = a_tag.get('href')
            if link is not None:
                print(link)
else:
    print('Failed to retrieve the web page.')

input()