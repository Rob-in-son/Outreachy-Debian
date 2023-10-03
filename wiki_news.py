#A script to read data from the News page on Debianwiki, parse the data and write it to a file in markdown
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md

#website page to be scrapped
url = "https://wiki.debian.org/News"
# read webpage
req = requests.get(url)
#Parse data
soup = BeautifulSoup(req.content, "html.parser")

html = (soup.prettify())
html_markdown = md(html)

#Create a file to store the markdown
markdown_file = open("Debian wiki news.txt", "x")

#Write to the file 
markdown_file.write(html_markdown)
