import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyscreenshot as ps

psid = 'YOUR-PSID'
password = 'YOUR-PASSWORD'
pdf_frame = '//*[@id="upload_document_player"]'


def screengrab(x1=0, y1=0, x2=1365, y2=767, name='Give me a NAME'):
    name = name + '.png'
    image = ps.grab(bbox=(x1, y1, x2, y2))
    image.save('C:\\Users\\Dell\\Pictures\\Screenshots\\e-Book2\\' + name)


def wait(extra=0):
    delay = random.uniform(3, 4+extra)
    time.sleep(delay)


def reach_ebook():
    try:
        wait()
        ad_close = driver.find_element_by_xpath('//*[@id="co-close-icon-5e5e5503c897f04cf04916ae"]')
        ad_close.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass

    login = driver.find_element_by_xpath('//*[@id="block-useraccountmenu"]/ul/li[1]/a')
    login.click()
    driver.implicitly_wait(10)

    enter_psid = driver.find_element_by_xpath('//*[@id="edit-name"]')
    enter_psid.send_keys(psid)

    enter_password = driver.find_element_by_xpath('//*[@id="edit-pass"]')
    enter_password.send_keys(password)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sign_in = driver.find_element_by_xpath('//*[@id="edit-submit"]')
    sign_in.click()
    wait()

    access_videos = driver.find_element_by_xpath('//*[@id="content-area"]/span/a')
    access_videos.click()

    driver.switch_to.window(driver.window_handles[-1])  # Switch to last open window.

    physics_ch3 = driver.find_element_by_xpath('//*[@id="courses-id-218201"]/a')
    physics_ch3.click()

    physics_ch3_topic = driver.find_element_by_xpath('//*[@id="title-text-218247"]/a')
    physics_ch3_topic.click()
    wait()

    driver.execute_script("window.scrollTo(0, 728)")

    ebook_ch3 = driver.find_element_by_xpath(
        '//*[@id="content-wrapper"]/div[1]/div[2]/div[2]/div/div[3]/div/a[1]/div/div/button')
    ebook_ch3.click()
#    driver.execute_script("window.scrollTo(0, 268)")
    wait(15)
    driver.switch_to.frame(pdf_frame)
    full_screen = driver.find_element_by_xpath('/html/body/div[1]/div[2]')
    full_screen.click()
    wait()


def gotcha(subject, chapter, page):
    wait(2)
    screengrab(252, 74, 1095, 767, name=f'{subject}-Ch{chapter}-Pg{page}-1')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    screengrab(252, 385, 1095, 754, name=f'{subject}-Ch{chapter}-Pg{page}-2')


def total_pages():
    frame = driver.find_element_by_xpath(pdf_frame)
    driver.switch_to.frame(frame)
    no_of_pages = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]')
    value = no_of_pages.get_attribute('value')
    driver.switch_to.default_content()
    return int(value)


def next_page():
    frame = driver.find_element_by_xpath(pdf_frame)
    driver.switch_to.frame(frame)
    next_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div')
    next_button.click()
    driver.switch_to.default_content()
    wait(3)


driver = webdriver.Chrome('PATH-TO-DRIVER')
driver.get('https://digital.aakash.ac.in/')
driver.maximize_window()


reach_ebook()
i = 1
pages = total_pages()
while i <= pages:
    gotcha('Physics', '03', i)
    next_page()
    i += 1
