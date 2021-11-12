import re
import glob
import time

from qbittorrent import Client
import os
import shutil
import mysql.connector as mysql
from datetime import datetime

while True:
    tmp = []
    with open("/data/link.txt") as file_in:
        for line in file_in:
            tmp.append(line)
    if tmp:
        db = mysql.connect(
            host="localhost",
            user="root",
            passwd="LRJ24CIFPxMbv7o+",
            database='phim'
        )
        cursor = db.cursor()
        for element in tmp:
            element = element.strip()
            try:
                qb = Client('http://' + element)
                qb.login('admin', 'adminadmin')
                completed = qb.torrents(filter='completed')

                if completed:
                    with open("/data/done.txt", "a") as myfile:
                        parent_list = os.listdir("/data/downloading")
                        for file in parent_list:
                            for e in completed:
                                try:
                                    name = re.sub(r'\(\d+\) \[.*\]', '', e['name']).strip()
                                except:
                                    name = e['name'].strip()
                                try:
                                    year = re.findall(r'\(\d+\)', e['name'])[0]
                                except Exception as ex:
                                    print(ex)
                                    continue
                                #print('aaa')
                                #print('----' +name)
                                if name in file:
                                    myfile.write(file + '\n')
                                    try:
                                        shutil.move('/data/downloading/' + file, '/data/downloaded/' + file)
                                        cursor = db.cursor()
                                        now = datetime.now()
                                        query = '''
                                        UPDATE phim set updateat=%s where TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(name), '#',''), '?', ''), "'", ''),"!", ''),",", ''),":", ''),"-", ''),".", ''),"&", '')) =%s and year=%s
                                        '''
                                        values = (now.strftime('%Y-%m-%d %H:%M:%S'), re.sub(' +', ' ', name.replace('#', '').replace('?', '').replace("'", '').replace('!', '').replace(',','').replace(':','').replace('-','').replace('.','').replace('&','').lower().strip()), year.replace('(','').replace(')',''))
                                        cursor.execute(query, values)
                                        db.commit()
                                    except Exception as ex:
                                        print(ex)
                                        print('error delete file')
            except Exception as ex:
                print('eeee')
                print(element)
        db.close()
    print('done')
    time.sleep(10)