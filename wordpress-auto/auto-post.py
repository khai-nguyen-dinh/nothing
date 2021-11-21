import random
import re
import urllib.request
import lxml.html
import requests
import json
import base64
import pymongo
from datetime import datetime, timedelta

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['data']
list_replace = [
    {
        'key': 'tôi',
        'value': 'ta'
    },
    {
        'key': 'DigitalOcean',
        'value': 'VNstack'
    },
    {
        'key': 'digitaldcean',
        'value': 'vnstack'
    },
    {
        'key': 'Digitaldcean',
        'value': 'VNstack'
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
        'key': 'webhoidap',
        'value': 'vnstack'
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


def download_image(url):
    name = random.randrange(10000000, 100000000)
    fullname = str(name) + ".jpg"
    try:
        urllib.request.urlretrieve(url, fullname)
    except:
        return None
    return fullname


def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json


def upload_image_to_wordpress(image, url, header_json):
    fileName = download_image(image)
    if fileName:
        print(fileName)
        media = {'file': open('./' + fileName, "rb"), 'caption': 'My great demo picture'}
        responce = requests.post(url + "wp-json/wp/v2/media", headers=header_json, files=media)
        out = ''
        try:
            raw = responce.json()
            print(raw['guid']['raw'])
            return raw['guid']['raw']
        except:
            return ''
    else:
        return ''


collection = db.digitalocean
count = 0
for post in collection.find():
    if count > 300:
        break
    else:
        count = count + 1
    # collection.update({"_id": post['_id']}, {
    #     "$set": {"link": post['link'].replace('https://translate.google.com/translate?sl=en&tl=vi&u=').strip()}})

    dt = datetime.now() + timedelta(days=-1)
    dt = dt.strftime("%Y-%m-%dT%X")
    website = "https://vnstack.com/wp-json/wp/v2/posts"
    user = "spadmin"
    password = ""
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    title = post['title']
    content = post['content']

    # content = re.sub('<a href="https://www-digitalocean-com.translate.goog.*/', '<a href="https://webhoidap.com/', content)
    # content = re.sub('\?_x_tr_sl.*?">', '">', content)
    # tim link anh
    list_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    # thay the link anh
    for url in list_url:
        if 'png' in url and 'vnstack' not in url:
            tmp = upload_image_to_wordpress(url, 'https://vnstack.com/', header)
            if tmp:
                content = content.replace(url, tmp)
        elif 'jpg' in url and 'vnstack' not in url:
            tmp = upload_image_to_wordpress(url, 'https://vnstack.com/', header)
            if tmp:
                content = content.replace(url, tmp)
        elif 'jpeg' in url and 'vnstack' not in url:
            tmp = upload_image_to_wordpress(url, 'https://vnstack.com/', header)
            if tmp:
                content = content.replace(url, tmp)
        else:
            continue
    for element in list_replace:
        content = content.replace(element['key'], element['value'])
    # lay tag bai viet
    tags = []
    try:
        response = requests.get(post['link'])
        tree = lxml.html.fromstring(response.text)
        title_elem = tree.xpath('//a[@class="tag"]//text()')
        for tag in title_elem:
            if 'digitalocean' not in tag:
                tags.append(tag)
    except Exception as e:
        print(e)

    # dang bai
    post = {
        'title': title.replace('DigitalOcean','VNstack'),
        'status': 'publish',
        'content': content,
        'categories': [28, 75],
        'tag': tags,
        'slug': post['link'].split('/')[-1].replace('digitalocean','vnstack'),
        'date': dt
    }
    responce = requests.post(website, headers=header, json=post)
    # xoa bai sau khi dang
    collection.delete_one({"_id": ObjectId(post['_id'])})
    print(responce.text)
