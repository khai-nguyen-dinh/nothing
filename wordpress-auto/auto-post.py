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
        'key': 'blog.digitalocean',
        'value': 'vnstack'
    },
    {
        'key': 'digitalocean',
        'value': 'vnstack'
    },
    {
        'key': 'Digitalocean',
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
    },
    {
        'key': 'https://translate.google.com/website?sl=en&amp;tl=vi&amp;nui=1&amp;u=',
        'value': ''
    },
    {
        'key': 'https://www-digitalocean-com.translate.goog/community/tutorial_series',
        'value': 'https://vnstack.com'
    }, {
        'key': '&_x_tr_sl=en&_x_tr_tl=vi&_x_tr_hl=en-US&_x_tr_pto=nui',
        'value': ''
    }, {
        'key': 'https://www-digitalocean-com.translate.goog/community/tutorials',
        'value': 'https://vnstack.com'
    },
    {
        'key': 'https://www-digitalocean-com.translate.goog/community/tags',
        'value': 'https://vnstack.com/tags'
    },
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
    webtags = ["88,Conceptual", "89,Configuration Management", "90,Container", "91,Control Panels", "92,Custom Images",
               "93,Data Analysis", "94,Databases", "95,Debian", "96,Debian 10", "97,Deployment",
               "98,Developer Education", "99,Development", "100,Django", "101,DNS", "102,Docker", "103,Drupal",
               "104,Elasticsearch", "105,Email", "106,FAQ", "20,fashion", "107,Fedora", "108,Firewall", "109,Flask",
               "110,Flutter", "111,GatsbyJS", "112,Getting Started", "27,git", "113,Glossary", "114,Go", "115,GraphQL",
               "116,HAProxy", "117,High Availability", "118,HTML", "119,Infrastructure", "120,Initial Server Setup",
               "121,Interactive", "122,IPv6", "123,Java", "124,JavaScript", "125,Kubernetes", "126,LAMP Stack",
               "84,Lập trình", "127,Laravel", "128,LEMP", "129,Let’s Encrypt", "130,Linux Basics", "131,Linux Commands",
               "132,Load Balancing", "133,Logging", "134,Machine Learning", "135,MariaDB", "136,MEAN",
               "137,Miscellaneous", "138,MongoDB", "139,Monitoring", "140,MySQL", "141,Networking", "142,Next.js",
               "143,Nginx", "144,Node.js", "145,NoSQL", "146,Object Storage", "147,Open Source", "148,PHP",
               "149,PHP Frameworks", "150,PostgreSQL", "151,Programming Project", "152,Python", "153,Python Frameworks",
               "154,Quickstart", "155,React", "156,Redis", "157,Rocky Linux", "158,Rocky Linux 8", "159,Ruby",
               "160,Ruby on Rails", "161,Scaling", "162,Security", "163,Server Optimization", "164,Slack",
               "165,Solutions", "166,Spin Up", "167,SQL", "168,SQLite", "169,System Tools", "170,Terraform",
               "171,TypeScript", "172,Ubuntu", "173,Ubuntu 16.04", "174,Ubuntu 18.04", "175,Ubuntu 20.04", "176,VPN",
               "177,VS Code", "17,Vue.js", "179,Workshop Kits"]
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
    final_tag = []
    for webtag in webtags:
        for tag in tags:
            if tag in webtag:
                final_tag.append(int(webtag.split(',')[0]))
    # dang bai
    new_post = {
        'title': title.replace('DigitalOcean', 'VNstack'),
        'status': 'publish',
        'content': content,
        'categories': [28, 75],
        'tag': final_tag,
        'slug': post['link'].split('/')[-1].replace('digitalocean', 'vnstack'),
        'date': dt
    }
    responce = requests.post(website, headers=header, json=new_post)
    # xoa bai sau khi dang
    collection.delete_one({"_id": post['_id']})
    print(responce.text)
