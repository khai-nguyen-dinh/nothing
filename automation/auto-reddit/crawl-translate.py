import time
from multiprocessing import Pool

import pymongo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.data


def run():
    options = webdriver.ChromeOptions()
    options.add_extension(r'C:\Users\WhatUpTime.com\Downloads\zenmate.crx')
    driver = webdriver.Chrome(options=options,
                              executable_path=r'C:\Users\WhatUpTime.com\Downloads\chromedriver.exe')
    driver.get('chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html')

    time.sleep(3)
    window_before = driver.window_handles[0]
    driver.switch_to.window(window_before)

    driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
    driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
    driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
    driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
    time.sleep(3)
    driver.find_element_by_class_name('inactive-shield').click()

    # time.sleep(3)
    # driver.find_element_by_xpath('//div[@class="location-container align-items-stretch ng-star-inserted"]').click()
    # time.sleep(3)
    # driver.find_element_by_xpath('//span[@id="country-browsing-DE"]').click()
    driver.get(line)
    ele = driver.find_element_by_tag_name('body')
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    ele.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    body = driver.find_element_by_xpath('//div[contains(@class,"content-body")]')
    title = driver.find_element_by_xpath('//h1[contains(@class,"content-title")]').text
    out = body.get_attribute('outerHTML')
    db.web.insert_one({'title': title, 'content': out})
    driver.quit()


if __name__ == "__main__":
    pool = Pool(processes=3)
    with open('linku.txt') as file:
        for line in file:
            pool.apply_async(run, args=(line,))
    print('======  apply_async  ======')
    pool.close()
    pool.join()
