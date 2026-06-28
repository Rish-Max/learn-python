import requests
from bs4 import BeautifulSoup
import csv

NUMBER_OF_BOOKS = 10
BASE_URL = "https://books.toscrape.com"
FIRST_BOOK_URL = f"{BASE_URL}/catalogue/page-1.html"

FILE_PATH = "books.csv"

def fetch_websites_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def scape_list_of_books(html):
    raw = BeautifulSoup(html,'html.parser')
    raw_books = raw.find_all('article', class_='product_pod') 
    return [{"Title":book.find('h3').find('a')['title'].strip(),"Price":book.find('p', class_='price_color').get_text().replace('Â', '').strip(),"Image":book.find('img')['src'].strip()} for book in raw_books]

def scape_next_page(html):
    raw = BeautifulSoup(html,'html.parser')
    raw_next_page = raw.find('li', class_='next')
    return f"{BASE_URL}/catalogue/{raw_next_page.find('a')['href']}" if raw_next_page else None

def save_image_locally(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open("images/" + filename, 'wb') as file:
            file.write(response.content)
    else:
        return None

def save_content_to_csv(content, filename):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price', 'Image'])
        writer.writeheader()
        writer.writerows(content)


    
def main():

    list_of_books = []
    url = FIRST_BOOK_URL
    while len(list_of_books) <= NUMBER_OF_BOOKS:
        html = fetch_websites_html(url)
        if html:
            books = scape_list_of_books(html)
            if len(books) + len(list_of_books) > NUMBER_OF_BOOKS:
                no_of_books_to_add = NUMBER_OF_BOOKS - len(list_of_books)
                list_of_books.extend(books[:no_of_books_to_add])
                break
            else:
                list_of_books.extend(books)
            url = scape_next_page(html)
        else:
            print("Failed to fetch website HTML")
            break
    for book in list_of_books:
        save_image_locally(f"{BASE_URL}/{book['Image'].replace('../', '')}", book['Title'] + '.jpg')
        book['Image'] = f"images/{book['Title']}.jpg"
    save_content_to_csv(list_of_books, FILE_PATH)

if __name__ == "__main__":
    main()