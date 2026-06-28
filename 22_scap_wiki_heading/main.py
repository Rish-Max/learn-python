import requests
from bs4 import BeautifulSoup

URL = "https://wiki.python.org/python/FrontPage.html"

def scrape_wiki_heading(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_headings = soup.find_all(['h1', 'h2'])
        headings_texts = [raw_heading.get_text().strip() for raw_heading in raw_headings]
        return headings_texts
    else:
        return None
    
print(scrape_wiki_heading(URL))