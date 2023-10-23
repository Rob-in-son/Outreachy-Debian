# Outreachy-Debian Project

## Project Overview

This project is designed to scrape data from the Debian News webpage, convert the fetched HTML content into markdown format, and then write this data into a markdown file. This allows for easy and readable access to the latest news updates from Debian in a simple markdown file.

## Environment Setup

1. Ensure you have Python 3.x installed on your machine. You can download and install Python via [Python's official site](https://www.python.org/).

2. It is recommended to use a virtual environment to manage the project dependencies separately. You can set up a virtual environment in Python using the following command:

```sh
python -m venv venv
```

Activate the virtual environment. On Windows, use:

```
.\venv\Scripts\activate
```

On Unix or MacOS, use:

```
source venv/bin/activate
```

Once you have your virtual environment setup and activated, install the project dependencies with:

```
pip install -r requirements.txt
```

## Running the Script

After setting up the environment and installing the dependencies, you can run the script using the following command:

```
python wiki_scraper.py
```

This command will execute the script, scrape the latest news from the Debian News webpage, convert it to markdown, and write it to the file output.md
