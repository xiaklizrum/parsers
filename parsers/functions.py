import requests
from bs4 import BeautifulSoup


def get_content_by_url(url):
    r = requests.get(url, headers={
        'User-Agent': (
            'Mozilla/5.0'
            '(X11; U; Linux x86_64; en-US; rv:1.9.1b3pre)'
            'Gecko/20090109 Shiretoko/3.1b3pre'
        )
    })
    return r.content


def get_tags_by_url(url, tag, _class):
    city_soup = BeautifulSoup(get_content_by_url(url), 'html.parser')
    try:
        tags = city_soup.find_all(tag, _class)
    except AttributeError:
        tags = []
    return tags
