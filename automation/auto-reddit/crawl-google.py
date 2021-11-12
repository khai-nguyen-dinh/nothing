from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension(r'/Users/mac/Downloads/sample/extension_8_0_3_0.crx')
driver = webdriver.Chrome(options=options,
                          executable_path=r'/Users/mac/Downloads/sample/chromedriver')
driver.get(
    'https://www.google.com/search?q=site%3Adigitalocean.com+tutorials&biw=1440&bih=821&sxsrf=AOaemvKLcVXPZWOX60KNep0Ga7CTGocdOg%3A1634895993442&ei=eYhyYaK1GuaYr7wPsOKl-Ak&ved=0ahUKEwji1buX3t3zAhVmzIsBHTBxCZ840gEQ4dUDCA4&uact=5&oq=site%3Adigitalocean.com+tutorials&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANKBAhBGABQAFgAYNeEAmgBcAJ4AIABAIgBAJIBAJgBAMgBCMABAQ&sclient=gws-wiz')

while True:
    for element in driver.find_elements_by_xpath('//div[@class="g"]//a'):
        f = open('link.txt', 'a')
        f.write(element.get_attribute('href') + '\n')
    driver.find_element_by_id('pnnext').click()
