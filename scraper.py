import requests
from bs4 import BeautifulSoup
import random

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def scrapewikilink(url):
    print(url)
    response = requests.get(url)
    # print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.string+'\n')

    allinks = soup.find(id="bodyContent").find_all('a')
    random.shuffle(allinks)

    # <a href="/wiki/Code_readability" class="mw-redirect" title="Code readability">code readability</a>
    for link in allinks:
        try:
            if link['href'].startswith('/wiki/'):
                newlink = "https://en.wikipedia.org"+link['href']
                scrapewikilink(newlink)
                break
        except KeyError:
            continue


scrapewikilink(url)
