import random
import time

import pyautogui
from selenium import webdriver
import redis

list_content = ['Just upvoted, can you upvote back?', 'An upvote from me! Could you perhaps send it a few of my posts?',
                'Upvoted !', 'Looking for some post karma! Just upvoted you. Can you please return?',
                'Upvoted all your recent posts! Please upvote back :)', 'Hey people! I need karma :( can you help me?',
                'Upvoted !', 'Upvoted plzzz']

pyautogui.FAILSAFE = False


def run(username):
    driver = None
    while True:
        # driver = webdriver.Firefox(
        #     executable_path=r'C:\Users\tranthienan240319\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe')
        # driver.maximize_window()
        # driver.install_addon(r'C:\Users\tranthienan240319\Downloads\zenmate_free_vpn-7.6.0.0-fx.xpi', temporary=True)
        # time.sleep(2)
        # print('start click')
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        # print(pyautogui.position())
        # pyautogui.moveTo(0, 500)
        # pyautogui.moveTo(1387, 65)
        # pyautogui.click()
        # time.sleep(2)
        # print(pyautogui.position())
        # pyautogui.moveTo(1276, 307)
        # pyautogui.click(clicks=5, interval=1.2)
        # time.sleep(2)
        # pyautogui.moveTo(1216, 513)
        # pyautogui.screenshot('button.png', region=(1216, 513, 250, 285))
        # pyautogui.click()
        # time.sleep(2)
        # pyautogui.moveTo(1118, 238)
        # pyautogui.click()
        # time.sleep(1)
        # pyautogui.moveTo(1276, 307)
        # pyautogui.click()
        # time.sleep(1)
        # window_before = driver.window_handles[0]
        # driver.switch_to_window(window_before)

        # remote
        # options = webdriver.ChromeOptions()
        # options.add_extension(r'/Users/mac/Downloads/sample/extension_8_0_3_0.crx')
        # driver = webdriver.Remote("http://localhost:4441/wd/hub", options=options)
        # driver.get('chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html')
        # time.sleep(3)
        # window_before = driver.window_handles[0]
        # driver.switch_to_window(window_before)

        options = webdriver.ChromeOptions()
        options.add_extension(r'C:\Users\tranthienan240319\Downloads\extension_8_0_3_0.crx')
        driver = webdriver.Chrome(options=options,
                                  executable_path=r'C:\Users\tranthienan240319\Downloads\chromedriver_win32\chromedriver')
        driver.get('chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html')
        time.sleep(3)
        window_before = driver.window_handles[0]
        driver.switch_to_window(window_before)

        driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
        driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
        driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
        driver.find_element_by_xpath('//div[@class="tour-container en"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="location-container align-items-stretch ng-star-inserted"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//span[@id="country-browsing-DE"]').click()
        driver.get('https://ifconfig.me/')
        ip = driver.find_element_by_id('ip_address').text
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
            'body > div > main > div.OnboardingStep.Onboarding__step.mode-auth > div > div.Step__content > form > fieldset:nth-child(8) > button').click()
        time.sleep(10)
        # vao group
        driver.get('https://old.reddit.com/r/FreeKarma4U/')
        time.sleep(5)
        # join group
        try:
            driver.find_element_by_xpath('//a[@class="option active add login-required"]').click()
        except:
            print('da join group')

        # lay list danh sach bai viet se comment
        list_post = []
        for i in range(4):
            tmp = driver.find_elements_by_xpath('//p[@class="title"]/a')
            for element in tmp:
                list_post.append(element.get_attribute('href'))
            driver.get(driver.find_element_by_xpath('//span[@class="next-button"]/a').get_attribute('href'))
        random.shuffle(list_post)
        count = 0
        for element in list_post:
            count = count + 1
            if count < 11:
                time.sleep(random.randint(8, 15))
                try:
                    driver.get(element)
                    driver.execute_script("scrollBy(0,200);")
                    driver.execute_script("scrollBy(0,200);")
                    driver.find_element_by_xpath('//div[@class="md"]/textarea').send_keys(random.choice(list_content))
                    driver.find_element_by_xpath('//button[@class="save"]').click()
                    time.sleep(random.randint(8, 15))
                except Exception as e:
                    print(e)
                    continue
            else:
                break
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()

    driver.close()
    driver.quit()
    return


if __name__ == '__main__':
    r = redis.StrictRedis(host='192.241.145.184', port=6379, db=1, password='Admin@0607', decode_responses=True)
    for key in r.scan_iter("user:*"):
        r.get(key)
