from flask import Flask, render_template, request
from flask import session

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
import mysql.connector as mysql

@app.route("/video/<id>", methods=['GET', 'POST'])
def video(id):
    # id = request.args['id']
    session.clear()
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="LRJ24CIFPxMbv7o+",
        database='phim'
    )
    cursor = db.cursor()
    query = 'select * from phim where imdb like "%{}%";'.format(id)
    cursor.execute(query)
    data = cursor.fetchone()
    raw = data[8].split('"')
    link = ''
    for e in raw:
        if '.mp4' in e or '.mkv' in e:
            link = e
            break
    if request.method == 'GET':
        return render_template('hello.html', link='https://gofastplayer.com/watch/' + link)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
