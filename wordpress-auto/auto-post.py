import re

import requests
import json
import base64
import pymongo
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['data']
list_replace = [
    {
        'key': 'tôi',
        'value': 'ta'
    },
    {
        'key': 'thùng chứa',
        'value': 'container'
    },
    {
        'key': 'sự kiện',
        'value': 'event'
    },
    {
        'key': 'vỏ',
        'value': 'shell'
    }, {
        'key': 'thiết bị đầu cuối',
        'value': 'terminal'
    }, {
        'key': 'quy trình',
        'value': 'tiến trình'
    }, {
        'key': 'cổng',
        'value': 'port'
    }, {
        'key': 'tệp',
        'value': 'file'
    }, {
        'key': 'mạng',
        'value': 'network'
    }, {
        'key': 'riêng tư',
        'value': 'private'
    }, {
        'key': 'khóa',
        'value': 'key'
    },
    {
        'key': 'mã',
        'value': 'code'
    },
    {
        'key': '<div class="toolbar"><div class="toolbar-item"><button><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sao chép</font></font></button></div></div></div>',
        'value': ''
    },
    {
        'key': 'nhà phát triển',
        'value': 'developer'
    },
    {
        'key': 'https://translate.google.com/website?sl=en&amp;tl=vi&amp;nui=1&amp;u=',
        'value': ''
    },
    {
        'key': 'https://www-digitalocean-com.translate.goog',
        'value': ''
    }, {
        'key': '?_x_tr_sl=en&amp;_x_tr_tl=vi&amp;_x_tr_hl=en-US&amp;_x_tr_pto=nui',
        'value': ''
    }
]
collection = db.digitalocean
for post in collection.find():
    # collection.update({"_id": post['_id']}, {
    #     "$set": {"link": post['link'].replace('https://translate.google.com/translate?sl=en&tl=vi&u=').strip()}})

    dt = datetime.now() + timedelta(days=-1)
    dt = dt.strftime("%Y-%m-%dT%X")
    url = "https://webhoidap.com/wp-json/wp/v2/posts"
    user = "adminadmin"
    password = "1JP9 km6E CNNi 5Omb sRVa vTDI"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    title = post['title']
    content = post['content']
    for element in list_replace:
        content = content.replace(element['key'], element['value'])
    # content = re.sub('<a href="https://www-digitalocean-com.translate.goog.*/', '<a href="https://webhoidap.com/', content)
    # content = re.sub('\?_x_tr_sl.*?">', '">', content)
    post = {
        'title': title,
        'status': 'publish',
        'content': content,
        'categories': [28, 75],
        'tag': '',
        'slug': post['link'].split('/')[-1],
        'date': dt
    }
    responce = requests.post(url, headers=header, json=post)
    print(responce.text)
