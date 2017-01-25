import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages: 
        url = "http://creativeworks.tistory.com/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('th > .current'):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_article(href)
        page = page + 1

def get_single_article(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')

    for contents in soup.select('p > span'):
        print(contents.text)

spider(5)
