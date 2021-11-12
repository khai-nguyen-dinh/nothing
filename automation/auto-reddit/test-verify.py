import time

from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options,
                          executable_path=r'/Users/mac/Downloads/sample/chromedriver')
driver.get('https://www.reddit.com/verification/eyJhY2NvdW50X2lkIjogInQyX2ZzYXhzcXB1IiwgInNpZyI6ICJBUUFBbWRSM1lSY1hhOHVhWXBWN0hXLXkzQnpBQVlxM1lYMEd6RXc4VmZEaFBBaEZlYTRkIn0?correlation_id=3D51ad724b-e3cb-4af7-a9a1-7de0a63cf5c1&amp;ref=3Dverify_email&amp;ref_campaign=3Dverify_email&amp;ref_source=3Demail')
time.sleep(3)
driver.find_element_by_class_name('verify-button').click()