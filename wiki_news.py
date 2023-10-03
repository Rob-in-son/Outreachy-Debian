#A script to read data from the News page on Debianwiki, parse the data and write it to a file in markdown
from bs4 import BeautifulSoup
import requests

#website page to be scrapped
url = "https://wiki.debian.org/News"
# read webpage
req = requests.get(url)
#Parse data
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

