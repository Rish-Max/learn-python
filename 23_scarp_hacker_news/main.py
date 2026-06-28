import csv
import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
FILE_PATH = "hacker_news.csv"

def fetch_websites_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def scrape_hacker_news_headings(html):
    raw = BeautifulSoup(html,'html.parser')
    raw_headings = raw.find_all('span', class_='titleline')
    return [{"Link":heading.find('a')['href'],"Heading":heading.find('a').get_text().strip()} for heading in raw_headings[:20]]

def save_content_to_csv(content, filename):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Link', 'Heading'])
        writer.writeheader()
        writer.writerows(content)

def main():
    html = fetch_websites_html(URL)
    if html:
        headings = scrape_hacker_news_headings(html)
        save_content_to_csv(headings, FILE_PATH)
    else:
        print("Failed to fetch website HTML")

if __name__ == "__main__":
    main()