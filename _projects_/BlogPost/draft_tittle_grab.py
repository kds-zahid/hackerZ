import requests
from bs4 import BeautifulSoup

# Replace this with the URL you want to fetch text from
url = 'https://www.latestdatabase.com/zh-CN/phone-number-list/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Determine the character encoding of the response
    encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)
    
    # Find the <h1> tag and extract its text
    h1_tag = soup.find('h1')
    
    if h1_tag:
        h1_text = h1_tag.get_text()
        # Print or store the extracted text
        print("Text within the <h1> tag:", h1_text)
    else:
        print("No <h1> tag found on the page.")
else:
    print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
