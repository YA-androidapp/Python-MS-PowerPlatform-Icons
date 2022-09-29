#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


import requests
from bs4 import BeautifulSoup
import re


target_url = 'https://learn.microsoft.com/ja-jp/connectors/connector-reference/connector-reference-powerautomate-connectors'
r = requests.get(target_url)
soup = BeautifulSoup(r.content, 'lxml', from_encoding='utf-8')
# print(soup.prettify())

table_elem = soup.select('table')[0]
# print(table_elem)

lines = table_elem.find_all('tr')
for line in lines:
    # print('タグ名:', line.name)
    img_elem = line.find('img')
    label_elem = line.find('b')
    if img_elem and label_elem:
        print(img_elem['src'], label_elem.decode_contents(formatter="html"))
