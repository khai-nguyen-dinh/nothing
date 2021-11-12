import time
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def run():
    source = requests.get("http://23.146.144.156:8082/phim").json()
    driver = webdriver.Chrome(
        executable_path='C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver')
    driver.get('https://gofastmovies.com/user/login')
    time.sleep(3)
    email = driver.find_element_by_id('login_email')
    email.send_keys('khaindinh@gmail.com')

    pw = driver.find_element_by_id('login_password')
    pw.send_keys('Admin@123')
    driver.find_element_by_id('submit-btn').click()

    for id in source['phim']:
        try:
            driver.get('https://gofastmovies.com/admin/videos_add/')

            find_id_imdb = driver.find_element_by_id('imdb_id')
            find_id_imdb.send_keys(id)
            find_movies = driver.find_element_by_id('import_btn')
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'import_btn')))
            find_movies.click()
            # copy ten phim
            while True:
                name_movies = driver.find_element_by_id('title').get_attribute('value')
                if name_movies == '':
                    continue
                else:
                    break
            # paste ten phim
            id_seo = driver.find_element_by_id('seo_title')
            id_seo.send_keys(name_movies)
            # copy mieu ta phim
            body_movies = driver.find_element_by_xpath('//div[@class="note-editable panel-body"]/p').text
            # paste body phim
            body_movies_s = driver.find_element_by_id("meta_description")
            body_movies_s.send_keys(body_movies)
            time.sleep(2)
            driver.find_element_by_css_selector('body > main > form > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(10) > div > button').click()
            done = requests.get("http://23.146.144.156:8082/" + id)
            print(done.status_code)
        except Exception as e:
            print(e)
    driver.close()


if __name__ == '__main__':
    run()
