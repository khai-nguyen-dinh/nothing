import random
import time

import pyautogui
from selenium import webdriver

link_web = ['https://videohamsterx.com/2021/10/10/happy-bithday-lana-rhoades/',
            'https://videohamsterx.com/2021/10/10/lea-lexis-gets-her-dream-gangbang/',
            'https://videohamsterx.com/2021/10/10/little-bailey-goes-outdoor-park-with-her-boyfriend-and-blowjob/',
            'https://videohamsterx.com/2021/10/10/the-smell-of-his'
            '-cock-drove-her-crazy-and-she-jumped-on-him-dickforlily/']

pyautogui.FAILSAFE = False
list_group = []


def run(username):
    while True:
        options = webdriver.ChromeOptions()
        options.add_extension(r'C:\Users\tranthienan240319\Downloads\extension_8_0_3_0.crx')
        driver = webdriver.Chrome(options=options,
                                  executable_path=r'C:\Users\tranthienan240319\Downloads\chromedriver_win32\chromedriver')
        driver.get('chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html')
        time.sleep(3)
        window_before = driver.window_handles[0]
        driver.switch_to_window(window_before)
        try:
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//div[@class="location-container align-items-stretch ng-star-inserted"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//span[@id="country-browsing-DE"]').click()
        except:
            continue

        driver.get('https://ifconfig.me/')
        ip = driver.find_element_by_id('ip_address').text
        # time.sleep(10000)
        print(ip)
        if ip.startswith('154') == False:
            driver.close()
            driver.quit()
            continue
        else:
            break
    try:
        # auto reddit
        driver.get('https://www.reddit.com/login/')
        time.sleep(3)
        # dang nhap
        email = driver.find_element_by_id('loginUsername')
        email.send_keys(username)
        pw = driver.find_element_by_id('loginPassword')
        pw.send_keys('SONkmaat10b@@@')
        driver.find_element_by_css_selector(
            'body > div > main > div.OnboardingStep.Onboarding__'
            'step.mode-auth > div > div.Step__content > form > fieldset:nth-child(8) > button').click()
        time.sleep(10)
        # Vao tung gr
        count = 0
        while True:

            count = count + 1
            if count > 30:
                break
            line = list_group.pop()
            driver.get(line)
            try:
                driver.find_element_by_xpath('//button[@value="yes"]').click()
            except:
                print('OK')
            try:
                driver.find_element_by_xpath('//a[@class="option active add login-required"]').click()
            except:
                print('da join group')
            try:
                time.sleep(5)
                driver.find_element_by_xpath('//html/body/div[3]/div[2]/div/div/a').click()
                time.sleep(5)
                url = driver.find_element_by_id('url')
                url.send_keys(random.choice(link_web))
                driver.find_element_by_xpath('//div[@id="suggest-title"]/button').click()
                time.sleep(10)
                driver.find_element_by_xpath('//button[@name="submit"]').click()
                f = open('group_ok.txt', 'a')
                f.write(line)
            except:
                ferror = open('grooup_error.txt', 'a')
                ferror.write(line)

    except Exception as e:
        print(e)
        driver.close()
        driver.quit()

    driver.close()
    driver.quit()
    return


if __name__ == '__main__':
    with open('listgroup.txt') as file:
        for line in file:
            list_group.append(line)
    with open('account.txt') as file:
        for line in file:
            run(line.strip())
