import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin

# Define constants
BASE_URL = "https://wiki.debian.org"
NEWS_URL = urljoin(BASE_URL, "News")
OUTPUT_FILE = "output.md"

def fetch_html(url):
    # Fetch the HTML content from the URL provided.# 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

        print(f"The content has been written to {OUTPUT_FILE}")
def correct_relative_links(soup):
    # Corrects the relative links in the HTML content to be absolute URLs.# 
    for a_tag in soup.find_all("a", href=True):
        if a_tag['href'].startswith('/'):
            a_tag['href'] = urljoin(BASE_URL, a_tag['href'])

def convert_html_to_markdown(html_content, exclude_div_text):
    # Converts the HTML content to Markdown.# 
    return md(html_content)

def remove_div(soup, exclude_div_text):
    # Remove the div based on exclude_div_text
    for div in soup.find_all("div"):
        if exclude_div_text in div.get_text():
            div.extract()

def write_to_file(content, file_name):
    # Writes content to the specified file.# 
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"The content has been written to {file_name}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    # Fetch the HTML content
    html_content = fetch_html(NEWS_URL)
    if html_content:
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Correct relative links
        correct_relative_links(soup)

        # The text to be excluded from the HTML
        exclude_div_text = "More Actions:"

        # Remove the specified div
        remove_div(soup, exclude_div_text)

        # Convert HTML to Markdown
        markdown_content = convert_html_to_markdown(str(soup), exclude_div_text)

        # Write the Markdown to a file
        write_to_file(markdown_content, OUTPUT_FILE)
    else:
        print("Failed to retrieve the content. Please check your internet connection or the URL.")
    
if __name__ == "__main__":
    main()

