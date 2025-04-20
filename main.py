'''# Load libraries for web scraping
from bs4 import BeautifulSoup
import requests

# Get a soup from a URL
url = 'https://web.archive.org/web/20200427175705/https://cottageinn.com/pick-a-location/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# Get all tags of a certain type from the soup
tags = soup.find_all('h3')

# Collect info from the tags
collect_info = []
for tag in tags:
    # Get info from tag
    info = tag.text
    collect_info.append(info)

# Print the info
print(collect_info)



# Get the webpages
# Load libraries for web scraping
from bs4 import BeautifulSoup
import requests

# Get a soup from multiple URLs
base_url = 'https://web.archive.org/web/20230128074139/https://www.si.umich.edu/people/'
endings = ['barbara-ericson', 'steve-oney', 'paul-resnick']
for ending in endings:
    url = base_url + ending
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # Get first tag of a certain type from the soup
    tag = soup.find('a', class_='item-teaser--heading-link')
    # Get info from tag
    info = tag.get('href')

    # Print the info
    print(info)

#

# find the news about robin brewer
from bs4 import BeautifulSoup
import requests

# Get a soup from multiple URLs
base_url = 'https://web.archive.org/web/20230128074139/https://www.si.umich.edu/people/'
endings = ['robin-brewer']
for ending in endings:
    url = base_url + ending
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # Extract info from the page
    # Get first tag of a certain type from the soup
    tag = soup.find('a', class_='item-teaser--heading-link')

    # Get link from tag
    info = tag.get('href')

    # Print the info
    print(info)
'''

# Load libraries for web scraping
from bs4 import BeautifulSoup
import requests

# Get a soup from multiple URLs
base_url = 'https://www.ratemyprofessors.com/professor/'
endings = ['2454833', '2239751']
for ending in endings:
    url = base_url + ending
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # Get all tags of a certain type from the soup
    tags = soup.find_all('div', class_="Comments__StyledComments-dzzyvm-0 jpfwLX")

    # Collect info from the tags
    collect_info = []
    for tag in tags:
        # Get info from tag
        info = tag.text
        collect_info.append(info)

    # Print the info
    print(collect_info)

'''
You’ll always get an empty list or no results because the comments 
are loaded after the page loads, with JavaScript.



🔥 Option 2: Use a tool that runs JavaScript like a browser
This is where Selenium or Playwright comes in.
They open a real browser window, load the page, wait for JS to run, 
and then let you extract the HTML.

'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# List of professor pages
base_url = 'https://www.ratemyprofessors.com/professor/'
endings = ['2454833', '2239751']

for ending in endings:
    url = base_url + ending
    driver.get(url)
    time.sleep(3)  # Let the JavaScript load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    comments = soup.find_all('div', class_='Comments__StyledComments-dzzyvm-0 jpfwLX')

    print(f"\n--- Comments for {ending} ---")
    for comment in comments:
        print(comment.text.strip())

driver.quit()


