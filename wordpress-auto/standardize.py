import re

from requests_html import HTMLSession
from lxml import html

session = HTMLSession()
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['data']

collection = db.digitalocean

link = []
list_replace = [
    {
        'key': 'tôi',
        'value': 'ta'
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
        'key': 'https://www-digitalocean-com.translate.goog/community/tutorial_series',
        'value': 'https://webhoidap.com'
    }, {
        'key': '?_x_tr_sl=en&amp;_x_tr_tl=vi&amp;_x_tr_hl=en-US&amp;_x_tr_pto=nui',
        'value': ''
    }, {
        'key': 'https://www-digitalocean-com.translate.goog/community/tutorials',
        'value': 'https://webhoidap.com'
    },
    {
        'key': 'https://www-digitalocean-com.translate.goog/community/tags',
        'value': 'https://webhoidap.com/tags'
    },
]
for post in collection.find():
#     doc = html.fromstring(post['content'])
#     link = link + doc.xpath('//a/@href')
# with open('digi.txt', 'a') as f:
#     for e in link:
#         if 'digitalocean' in e and 'webhoidap' not in e:
#             # a = e.split('/')
#             # del a[-1]
#             # try:
#             #     del a[-1]
#             # except:
#             #     continue
#             f.write(e + '\n')
    # r = session.get(post['link'])
    # tmp = []
    # for e in r.html.links:
    #     if 'tags/' in e:
    #         tmp.append(e.split('/')[-1])

    content = post['content']
    for element in list_replace:
        content = content.replace(element['key'], element['value'])
    # content = re.sub('\?_x_tr_sl.*?">', '">', content)
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/tags','https://webhoidap.com/tags')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/books/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/articles/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/curriculums/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community"','https://webhoidap.com"')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community"','https://webhoidap.com"')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/tutorial_collections/','https://webhoidap.com/')
    # content =content.replace('https://translate.google.com/translate?sl=en&tl=vi&u=https://www.digitalocean.com/community/tutorials/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/cheatsheets','https://webhoidap.com')
    # content =content.replace('https://digitalocean.com/community/articles/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/docs/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/community/community_tags/','https://webhoidap.com/')
    # content =content.replace('https://www-digitalocean-com.translate.goog/products/','https://webhoidap.com/')
    content =content.replace('https://hacktoberfest.digitalocean.com/','https://webhoidap.com/')
    content =content.replace('https://www-digitalocean-com.translate.goog/company/blog/','https://webhoidap.com/')
    content =content.replace('https://www-digitalocean-com.translate.goog/company/blog/','https://webhoidap.com/')
    content =content.replace('https://www-digitalocean-com.translate.goog/company/blog/','https://webhoidap.com/')
    collection.update_one({"_id": post['_id']}, {
        "$set": {"content": content}})
