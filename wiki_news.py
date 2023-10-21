import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin

# Define constants
BASE_URL = "https://wiki.debian.org"
NEWS_URL = urljoin(BASE_URL, "News")
OUTPUT_FILE = "output.md"
# The div text to be excluded from the HTML
exclude_div_text = "More Actions:"

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def correct_relative_links(soup):
    for a_tag in soup.find_all("a", href=True):
        if a_tag['href'].startswith('/'):
            a_tag['href'] = urljoin(BASE_URL, a_tag['href'])

def convert_html_to_markdown(soup):
    return md(str(soup))

def remove_div(soup, exclude_div_text):
    for div in soup.find_all("div"):
        if exclude_div_text in div.get_text():
            div.extract()

def write_to_file(content, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"The content has been written to {file_name}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    html_content = fetch_html(NEWS_URL)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract the target line
        target_line_tag = soup.find(string="Debian has several news feeds, that can be interesting for different audiences, depending on how they use Debian:")
        target_line_text = ""
        if target_line_tag:
            target_line_text = target_line_tag.string + "\n\n"
            target_line_tag.extract()

        correct_relative_links(soup)
        remove_div(soup, exclude_div_text)
        
        markdown_content = convert_html_to_markdown(soup)

        # Adjust the desired markdown format for "General news"
        undesired_line = "General news\n"
        desired_line = "\n\n## General news\n"
        markdown_content = markdown_content.replace(undesired_line, desired_line)

        write_to_file(markdown_content, OUTPUT_FILE)
    else:
        print("Failed to retrieve the content. Please check your internet connection or the URL.")

if __name__ == "__main__":
    main()
