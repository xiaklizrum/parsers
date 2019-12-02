import csv
import os
from bs4 import BeautifulSoup
from parsers.functions import get_content_by_url, get_tags_by_url

ROOT_URL = 'https://zadarma.com/ru/tariffs/numbers/'


def get_td_list(html):
    tds = html.find_all('td')
    useless_td_text = ['Купить', 'Buy', '']
    return [__.text.strip() for __ in tds if __ not in useless_td_text]


def get_url(html, root):
    return '{}{}'.format(root, html.find('a').get('href'))


def city_format(row):
    try:
        return [
            row[0],
            row[1][0:-2] if row[1][-1].isdigit() and row[1][-2].isspace() else row[1],
            int(row[2].replace('руб', '')) if row[2].count('руб') == 1 else '',
            int(row[3].replace('руб', '')) if row[3].count('руб') == 1 else ''
        ]
    except IndexError:
        return []


if __name__ == '__main__':
    result_file_path = '{}/results/price.csv'.format(
        os.path.dirname(os.path.abspath(__file__))
    )
    tr_classes = {
        'class': ['flex-table__tr common', 'flex-table__tr favorite']
    }
    with open(result_file_path, 'w', newline='') as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL
        )
        country_trs = get_tags_by_url(ROOT_URL, 'tr', tr_classes)
        for country_tr in country_trs:
            country_td = get_td_list(country_tr)
            city_url = get_url(country_tr, ROOT_URL)
            city_trs = get_tags_by_url(city_url, 'tr', tr_classes)
            for city_tr in city_trs:
                city_td = city_format(get_td_list(city_tr))
                city_td.insert(1, country_td[1])
                city_td.append(get_url(city_tr, 'https://zadarma.com'))
                spamwriter.writerow(city_td)
                print(city_td)
