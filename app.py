#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


from bs4 import BeautifulSoup
import os
import requests


SAVEDIR = 'images\\Power Platform Connector'
target_url = 'https://learn.microsoft.com/ja-jp/connectors/connector-reference/connector-reference-powerautomate-connectors'


# https://api.github.com/repos/YA-androidapp/Python-MS-PowerPlatform-Icons/git/trees/main?recursive=1


def wget(url, file_name):
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(os.path.join(SAVEDIR, file_name), 'wb') as f:
                f.write(r.content)
        else:
            print(e, url, file_name)
    except Exception as e:
        print(e, url, file_name)

def main():
    r = requests.get(target_url)
    soup = BeautifulSoup(r.content, 'lxml', from_encoding='utf-8')
    # print(soup.prettify())

    table_elem = soup.select('table')[0]
    # print(table_elem)

    lines = table_elem.find_all('tr')
    for line in lines:
        img_elem = line.find('img')
        label_elem = line.find('b')
        if img_elem and label_elem:
            # print(img_elem['src'], label_elem.decode_contents(formatter="html"))
            extension = os.path.splitext(img_elem['src'])[1]
            wget(img_elem['src'], label_elem.decode_contents(formatter="html") + extension)


if __name__ == "__main__":
    main()
