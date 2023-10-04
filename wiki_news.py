#A script to read data from the News page on Debianwiki, parse the data and write it to a file in markdown
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md

# URL of the page to be scraped
url = "https://wiki.debian.org/News"


# Fetch the web page
response = requests.get(url)
response.raise_for_status()  # Ensure we got a valid response


# Parse the web page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


# Function to convert parsed HTML to markdown
def html_to_markdown(soup):
    markdown_output = ""
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    anchor_tags = soup.find_all('a')

    # Iterate through each anchor tag and replace it with the Markdown link
    for anchor in anchor_tags:
        markdown_link = md(str(anchor))
        anchor.replace_with(markdown_link)

    for header in headers:
        # Create markdown headers
        markdown_output += "#" * int(header.name[1]) + " " + header.get_text() + "\n\n"


        # Handle the possible following paragraph
        for sibling in header.find_next_siblings():
            if sibling.name and "h" in sibling.name:
                break
            markdown_output += sibling.get_text() + "\n\n"
    
    return markdown_output


# Convert HTML to markdown
markdown_output = html_to_markdown(soup)


# Write markdown to file
output_file_name = "output.md"
with open(output_file_name, 'w', encoding='utf-8') as file:
    file.write(markdown_output)


print(f"The content has been written to {output_file_name}")

