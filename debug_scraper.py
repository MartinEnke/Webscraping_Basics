# Get the webpage
# Load libraries for web scraping
from bs4 import BeautifulSoup
import requests

# Get a soup from a URL
url = 'https://www.hshv.org/petsoftheweek/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# Get info from one tag
# Get first tag of a certain type from the soup
tag = soup.find('a', class_='pt-cv-none cvplbd')
# Get info from tag
info = tag.text

# Print the info
print(info)

#
# span class=p--small


# Get a soup from a URL
url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# Get info from one tag
# Get first tag of a certain type from the soup
tag = soup.find('span', class_='p--small')
# Get info from tag
info = tag.text

# Print the info
print(info)


url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# Get all tags of a certain type from the soup
tags = soup.find_all('span', class_='p--small')

# Collect info from the tags
collect_info = []
for tag in tags:
    # Get info from tag
    info = tag.text
    collect_info.append(info)

# Print the info
print(collect_info)