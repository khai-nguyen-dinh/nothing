import json
import os
from qbittorrent import Client
import re
import time
import mysql.connector as mysql

# App config.

qb = Client('http://localhost:8081/')
qb.login('admin', 'adminadmin')
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="LRJ24CIFPxMbv7o+",
    database='phim'
)
cursor = db.cursor()
parent_list = os.listdir("/data/movies-raw")
i = 0
with open("error.txt", "a") as myfile:
    for file in parent_list:
        print(i)
        i = i + 1
        qb.delete_all()
        torrent_file = open('/data/movies-raw/' + file, 'rb')
        try:
            qb.download_from_file(torrent_file)
        except Exception as e:
            print(e)
        print('step2')
        completed = qb.torrents()
        for e in completed:
            try:
                while True:
                    files = qb.get_torrent_files(e['hash'])
                    if '[' in e['name']:
                        name = re.sub(r'\(\d+\) \[.*\]', '', e['name']).strip()
                    else:
                        name = e['name']
                    year = re.findall(r'\(\d+\)', e['name'])[0]
                    year = year.replace(')', '').replace('(', '')
                    tmp = []
                    for file in files:
                        tmp.append(file['name'])
                    if tmp:
                        query = '''
                            UPDATE phim set folder=%s where TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(name), '#',''), '?', ''), "'", ''),"!", ''),",", ''),":", ''),"-", ''),".", ''),"&", '')) =%s and year=%s
                            '''
                        values = (
                            json.dumps(tmp),
                            re.sub(' +', ' ', name.replace('#', '').replace('?', '').replace("'", '').replace('!', '').replace(',','').replace(':','').replace('-','').replace('.','').replace('&','').lower().strip()),
                            year)
                        cursor.execute(query, values)
                        db.commit()
                        break
            except Exception as a:
                print(e)
                print(e['name'])
                myfile.write(e['name'] + '\n')
        print('done')
