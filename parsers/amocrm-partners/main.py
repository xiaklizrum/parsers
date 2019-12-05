import os
import csv
from parsers.functions import get_content_by_url, get_tags_by_url


ROOT_URL = 'https://www.amocrm.ru'


if __name__ == '__main__':
    result_file_path = '{}/results/partners.csv'.format(
        os.path.dirname(os.path.abspath(__file__))
    )
    with open(result_file_path, 'w', newline='') as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL
        )
        partner_page = get_tags_by_url(
            ROOT_URL + '/partners',
            'a',
            {'class': 'partners-list__block'}
        )
        for item in partner_page:
            print(ROOT_URL + item.get('href'))
            partner_page_content = get_tags_by_url(
                ROOT_URL + item.get('href'),
                'div',
                {'class': 'partners-detail__contacts'}
            )[0]
            partner_page_header = get_tags_by_url(
                ROOT_URL + item.get('href'),
                'h2',
                {'class': 'partners-detail__page-title'}
            )[0]
            result = []
            result.append(partner_page_header.text.strip())
            result.append(ROOT_URL + item.get('href'))
            p_tags = partner_page_content.find_all('p')
            result.extend([
                result.append(item.text.replace('\n', '').strip())
                for __ in p_tags if item.text
            ])
            spamwriter.writerow(result)
