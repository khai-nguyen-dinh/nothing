import json
import os
import shutil
import random
import string
from flask import Flask, render_template, request, url_for
from flask import session
from qbittorrent import Client
from werkzeug.utils import redirect
from wtforms import Form

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
import mysql.connector as mysql


class ReusableForm(Form):
    @app.route("/", methods=['GET', 'POST'])
    def start():
        session.clear()
        db = mysql.connect(
            host="localhost",
            user="root",
            passwd="LRJ24CIFPxMbv7o+",
            database='phim'
        )
        form = ReusableForm(request.form)

        cursor = db.cursor()
        query = "SELECT * from phim where `update` is null ORDER BY `updateat` DESC limit 300 ;"
        cursor.execute(query)

        raw = cursor.fetchall()
        query = "SELECT count(*) from phim where `update` is null and `updateat` is not null;"
        cursor.execute(query)

        number = cursor.fetchone()
        db.close()
        data = []
        for element in raw:
            id = ''
            if element[8] and element[7]:
                id = element[2].replace('https://www.imdb.com/title/', '').replace('/', '')
                data.append([element[0], element[1], id, 'https://gofastplayer.com/video/' + id, element[7]])

        if request.method == 'POST':
            host = request.form['name']
            host = host.replace('http://', '').replace('/', '')
            qb = Client('http://{}/'.format(host))
            check = 0
            with open("/data/link.txt") as file_in:
                for line in file_in:
                    if host.strip() == line.strip():
                        check = 1
            if check == 0:
                with open("/data/link.txt", "a") as myfile:
                    myfile.write(host + '\n')
            qb.login('admin', 'adminadmin')
            parent_list = os.listdir("/data/movies")
            count = 0
            for child in parent_list:
                if check == 0:
                    if count < 300:
                        torrent_file = open("/data/movies/" + child, 'rb')
                        shutil.move('/data/movies/' + child, '/data/downloading/')
                        qb.download_from_file(torrent_file)
                    else:
                        break
                    count = count + 1
            return redirect(url_for('start'))
        return render_template('hello.html', form=form, data=data, number=number[0])

    @app.route("/<id>", methods=['GET', 'POST'])
    def hello(id):
        session.clear()
        db = mysql.connect(
            host="localhost",
            user="root",
            passwd="LRJ24CIFPxMbv7o+",
            database='phim'
        )
        db1 = mysql.connect(
            host="localhost",
            user="root",
            passwd="LRJ24CIFPxMbv7o+",
            database='gofastmovies'
        )
        form = ReusableForm(request.form)

        cursor = db.cursor()
        cursor1 = db1.cursor()
        # get id phim was imported
        query = "SELECT `videos_id`` from videos where `imdbid`='{}';".format(id)
        cursor1.execute(query)
        videoid = cursor1.fetchone()
        if videoid:
            letters = string.ascii_lowercase
            letter = (''.join(random.choice(letters) for i in range(10)))
            query = "INSERT INTO video_file(`video_file_id`,`stream_key`,`videos_id`,`file_source`,`source_type`,`file_url`,`label`,`order`) VALUE (%s,%s,%s,%s,%s,%s,%s,%s);"
            values = (None, letter, videoid[0], 'embed', 'link', 'https://gofastplayer.com/video/' + id, 'Server 1', 1)
            cursor1.execute(query, values)
            db1.commit()
            db1.close()

        # update imported
        if id:
            query = "UPDATE phim set `update`=%s where `imdb`=%s;"
            cursor.execute(query, ('yes', 'https://www.imdb.com/title/{}/'.format(id)))
            db.commit()
        query = "SELECT * from phim where `update` is null ORDER BY updateat DESC limit 100 ;"
        cursor.execute(query)

        # featch all data
        raw = cursor.fetchall()
        query = "SELECT count(*) from phim where `update` is null and `updateat` is not null;"
        cursor.execute(query)

        number = cursor.fetchone()
        db.close()
        data = []
        for element in raw:
            id = ''
            if element[8] and element[7]:
                id = element[2].replace('https://www.imdb.com/title/', '').replace('/', '')
                data.append([element[0], element[1], id, 'https://gofastplayer.com/video/' + id, element[7]])

        if request.method == 'POST':
            host = request.form['name']
            host = host.replace('http://', '').replace('/', '')
            qb = Client('http://{}/'.format(host))
            check = 0
            with open("/data/link.txt") as file_in:
                for line in file_in:
                    if host.strip() == line.strip():
                        check = 1
            if check == 0:
                with open("/data/link.txt", "a") as myfile:
                    myfile.write(host + '\n')
            qb.login('admin', 'adminadmin')
            parent_list = os.listdir("/data/movies")
            count = 0
            for child in parent_list:
                if check == 0:
                    if count < 300:
                        torrent_file = open("/data/movies/" + child, 'rb')
                        shutil.move('/data/movies/' + child, '/data/downloading/')
                        qb.download_from_file(torrent_file)
                    else:
                        break
                    count = count + 1
            return redirect(url_for('hello'))
        return render_template('hello.html', form=form, data=data, number=number[0])

    @app.route("/phim", methods=['GET', 'POST'])
    def phim():
        session.clear()
        db = mysql.connect(
            host="localhost",
            user="root",
            passwd="LRJ24CIFPxMbv7o+",
            database='phim'
        )
        form = ReusableForm(request.form)

        cursor = db.cursor()

        query = "SELECT * from phim where `update` is null and `updateat` is not null ORDER BY updateat DESC ;"
        cursor.execute(query)

        raw = cursor.fetchall()
        db.close()
        data = []
        for element in raw:
            data.append(element[2].replace('https://www.imdb.com/title/', '').replace('/', ''))
        return json.dumps({'phim': data})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
