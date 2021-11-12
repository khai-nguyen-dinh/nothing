import re
import glob
import time

from qbittorrent import Client
import os
import shutil
import mysql.connector as mysql
from datetime import datetime

while True:
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="LRJ24CIFPxMbv7o+",
        database='phim'
    )
    cursor = db.cursor()
    parent_list = os.listdir("/data/downloaded")
    for raw in parent_list:
        file = raw.replace('.torrent', '')
        try:
            name = re.sub(r'\(\d+\) \[.*\]', '', file.strip())
        except:
            name = file.strip().split(' (')[0]
        try:
            year = re.findall(r'\(\d+\)', file)[0]
        except Exception as ex:
            print(ex)
            continue
        query = '''
        SELECT * from phim where TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(name), '#',''), '?', ''), "'", ''),"!", ''),",", ''),":", ''),"-", ''),".", ''),"&", ''))=%s and year=% ;
        '''
        values = (re.sub(' +', ' ', name.replace('#', '').replace('?', '').replace("'", '').replace('!', '').replace(',','').replace(':','').replace('-','').replace('.','').replace('&','').lower().strip()), year.replace('(','').replace(')',''))
        cursor.execute(query, values)
        number = cursor.fetchone()
        if number:
            print(number[1])
            shutil.move('/data/downloaded/' + raw, '/data/pass/' + raw)

    print('done')
    time.sleep(10)
