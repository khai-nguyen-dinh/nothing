import requests
import base64
import random
import urllib.request


def download_image(url):
    name = random.randrange(10000000, 100000000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)
    return fullname


def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json


def upload_image_to_wordpress(image, url, header_json):
    fileName = download_image(image)
    print(fileName)
    media = {'file': open('./' + fileName, "rb"), 'caption': 'My great demo picture'}
    responce = requests.post(url + "wp-json/wp/v2/media", headers=header_json, files=media)
    newDict = responce.json()
    print(newDict['guid']['raw'])


hed = header("spadmin", "OVHn oknw iXHO hZr9 FMLs G8Qc")
upload_image_to_wordpress('http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg',
                          'https://vnstack.com/', hed)
