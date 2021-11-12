from bson import ObjectId
from requests_html import HTMLSession
from lxml import html

session = HTMLSession()
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['data']

collection1 = db.digitalocean
collection2 = db.tmp

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
]
for post in collection1.find():
    #     doc = html.fromstring(post['content'])
    #     link = link + doc.xpath('//a/@href')
    # for e in link:
    #     if 'digitalocean' in e:
    #         print(e)
    # r = session.get(post['link'])
    # tmp = []
    # for e in r.html.links:
    #     if 'tags/' in e:
    #         tmp.append(e.split('/')[-1])

    # content = post['content']
    # for element in list_replace:
    #     content = content.replace(element['key'], element['value'])
    tmp = collection2.find_one({'_id': ObjectId(post['_id'])})
    collection1.update_one({"_id": tmp['_id']}, {
        "$set": {"content": tmp['content']}})
