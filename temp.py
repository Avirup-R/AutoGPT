import requests
from bs4 import BeautifulSoup

# Replace this URL with the website you want to scrape
url = 'https://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396'

# Step 1: Fetch the website's HTML content
response = requests.get(url)
response.raise_for_status()  # Check for any request errors

# Step 2: Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')  # You can use a different parser if needed

# Step 3: Extract the text from the parsed HTML
# In this example, we'll extract all the text within <p> tags
paragraphs = soup.find_all('p')

# Concatenate the text from all paragraphs into a single string
website_text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

print(website_text)
