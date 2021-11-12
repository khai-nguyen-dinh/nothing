import datetime
from multiprocessing import Pool

import redis
from selenium import webdriver
import requests, time
import imaplib
import email
import re
import secrets

from email.mime.multipart import MIMEMultipart

API_KEY = 'e6170c2055d459d67cf71205590d9973'
data_sitekey = '6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC'
page_url = 'https://www.reddit.com/account/register/'


def run(raw):
    r = redis.StrictRedis(host='192.241.145.184', port=6379, db=0, password='Admin@0607')
    if r.exists('user:' + raw.split('|')[0]):
        return
    password = secrets.token_urlsafe(10)
    while True:
        options = webdriver.ChromeOptions()
        options.add_extension(r'C:\Users\WhatUpTime.com\Downloads\zenmate.crx')
        driver = webdriver.Chrome(options=options,
                                  executable_path=r'C:\Users\WhatUpTime.com\Downloads\chromedriver')
        driver.get('chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html')
        time.sleep(3)
        window_before = driver.window_handles[0]
        driver.switch_to.window(window_before)
        try:
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            time.sleep(3)
            driver.find_element_by_xpath(
                '//div[@class="location-container align-items-stretch ng-star-inserted"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//span[@id="country-browsing-DE"]').click()
        except:
            driver.quit()
        time.sleep(3)
        # check ip xem co bat dau voi 154 khong
        # driver.get('https://ifconfig.me/')
        # ip = driver.find_element_by_id('ip_address').text
        # print(ip)
        # if ip.startswith('154') == False:
        # driver.quit()
        # continue
        # else:
        # break
        break
    try:
        # auto reddit
        driver.get('https://www.reddit.com/account/register/')
        driver.find_element_by_id('regEmail').send_keys(raw.split('|')[0])
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="emailPermission"]').click()
        time.sleep(3)
        driver.find_element_by_css_selector(
            'body > div > main > div:nth-child(1) > div > div.Step__content > form > '
            'fieldset.AnimatedForm__field.m-small-margin > button').click()
        time.sleep(5)
        driver.find_element_by_id('regUsername').click()
        name = driver.find_element_by_xpath('//*[@class="Onboarding__usernameSuggestion"]').text

        driver.find_element_by_id('regUsername').send_keys(name)
        time.sleep(2)
        driver.find_element_by_id('regPassword').click()
        driver.find_element_by_id('regPassword').send_keys(password)
        time.sleep(5)
        driver.find_element_by_css_selector('body > div > main > div:nth-child(2) > div > div > '
                                            'div.AnimatedForm__bottomNav > button').click()

        # requets recaptcha
        u1 = f"https://2captcha.com/in.php?key=" \
             f"{API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
        r1 = requests.get(u1)
        print(r1.json())
        rid = r1.json().get("request")
        u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
        time.sleep(5)
        while True:
            r2 = requests.get(u2)
            print(r2.json())
            if r2.json().get("request") == "ERROR_CAPTCHA_UNSOLVABLE":
                with open('hotmail_eror.txt', 'a') as f:
                    f.writelines(raw)
                driver.close()
                try:
                    driver.quit()
                    return
                except:
                    return
            if r2.json().get("status") == 1:
                form_tokon = r2.json().get("request")
                print(form_tokon)
                break
            time.sleep(5)
        wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
        driver.execute_script(wirte_tokon_js)
        time.sleep(3)
        try:
            # singup reddit
            driver.find_element_by_xpath('//*[@class="AnimatedForm__submitButton SignupButton"]').click()
            time.sleep(10)
            # chon group reddit
            if driver.find_element_by_xpath('//*[@class="AnimatedForm__submitButton SubscribeButton"]'):
                driver.find_element_by_xpath('//*[@class="SubredditPicker__subreddit"]'
                                             '[1]/button[@class="AnimatedForm__subscribeButton "]').click()
                driver.find_element_by_xpath('//*[@class="SubredditPicker__subreddit"]'
                                             '[3]/button[@class="AnimatedForm__subscribeButton "]').click()
                driver.find_element_by_xpath('//*[@class="SubredditPicker__subreddit"]'
                                             '[4]/button[@class="AnimatedForm__subscribeButton "]').click()
                driver.find_element_by_xpath('//*[@class="SubredditPicker__subreddit"]'
                                             '[5]/button[@class="AnimatedForm__subscribeButton "]').click()
                time.sleep(5)
                driver.find_element_by_xpath('//*[@class="AnimatedForm__submitButton SubscribeButton"]').click()
            else:
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[4]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[2]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[8]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[9]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[10]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[17]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/button[19]').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div[2]/button').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div/div/div/button').click()
                driver.find_element_by_xpath(
                    '//html/body/div/div/div[2]/div[4]/div/div/div/div/div/div[3]/button').click()
                driver.find_element_by_xpath(
                    '//html/body/div/div/div[2]/div[4]/div/div/div/div/div/div[9]/button').click()
                driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div[2]/button').click()
                try:
                    driver.find_element_by_xpath('//html/body/div/div/div[2]/div[4]/div/div/div/div[2]/button').click()
                except:
                    pass
            time.sleep(10)
            # hotmail login
            mail = imaplib.IMAP4_SSL('outlook.office365.com')
            user_mail = raw.split('|')[0]
            pass_mail = raw.split('|')[1]
            mail.login(user_mail, pass_mail)
            mail.list()
            mail.select('inbox')
            verify_link = ''
            for i in range(1, 5):
                typ, msg_data = mail.fetch(str(i), '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(str(response_part[1]))
                        text = str(msg).replace(r'=\r\n', '')
                        print('333333333333333333')
                        try:
                            verify_link = re.search('https://www.reddit.com/verification/(.+?)ref_source=3Demail',
                                                    text).group()
                        except AttributeError:
                            found = ''
            mail.close()
            mail.logout()
            print(verify_link)
            driver.get(verify_link)
            time.sleep(5)
            # day account da tao vao redis de luu tru
            x = datetime.datetime.now()
            create_day = x.strftime("%D")
            name = str(name)
            name_tr = name + '|' + password + '|' + create_day
            # luu vao redis
            r.set('user:' + raw.split('|')[0], name_tr)
            driver.close()
            driver.quit()
        except Exception as ax:
            # luu hotmail dky loi
            reg_error = open('register_error.txt', 'a')
            reg_error.write(raw + '\n')
            driver.close()
            driver.quit()
            pass
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
    try:
        driver.quit()
    except:
        return
    return


if __name__ == '__main__':
    # chinh so luong can chay
    pool = Pool(processes=5)
    with open('hotmail.txt') as file:
        for line in file:
            pool.apply_async(run, args=(line.strip(),))
    print('======  apply_async  ======')
    pool.close()
    pool.join()
