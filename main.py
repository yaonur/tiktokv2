from selenium import webdriver
import undetected_chromedriver.v2 as uc
from time import sleep
from bs4 import BeautifulSoup as bf
import image_process
import paths_and_classes as pc
import helper_functions as hf
import passwords

options = uc.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument('--no-sandbox')
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_argument('--headless')
# driver = webdriver.Chrome('chromedriver.exe',options=options)
driver = uc.Chrome(options=options)


def start_bot():
    driver.get('https://www.tiktok.com/')
    hf.pass_driver(driver)


def destroy_landing_captcha():
    image_process.check_chaptcha_and_destroy(driver, pc.captcha_landing_xpath,pc.gap_image_xpath)


def destroy_login_captcha():
    iframe = hf.find_xpath(pc.iframe)
    if iframe:
        driver.switch_to.frame(iframe)
    else:
        iframe = hf.find_xpath(pc.iframe2)
        driver.switch_to.frame(iframe)
    image_process.check_chaptcha_and_destroy(driver, pc.captcha_login_xpath,pc.gap_image_login_xpath)
    driver.switch_to.default_content()

def login():
    try:
        login_button_landing = hf.find_xpath(pc.login_button_landing_xpath, 'login button landing')
        if login_button_landing:
            login_button_landing.click()
    except:
        pass

    iframe = hf.find_xpath(pc.iframe)
    if iframe:
        driver.switch_to.frame(iframe)
    else:
        iframe=hf.find_xpath(pc.iframe2)
        driver.switch_to.frame(iframe)

    login_with_email = hf.find_xpath(pc.login_with_email_xpath, 'login with email')
    login_with_email.click()

    login_with_email_popup = hf.find_xpath(pc.login_with_email_popup_xpath, 'login with email popup')
    login_with_email_popup.click()

    email_textbox = hf.find_xpath(pc.email_textbox_xpath, 'email textbox')
    email_textbox.send_keys(passwords.user_name)

    password_textbox = hf.find_xpath(pc.password_textbox_xpath, 'password textbox')
    password_textbox.send_keys(passwords.user_password)

    login_button_popup = hf.find_xpath(pc.login_button_popup_xpath, 'login button xpaath')
    login_button_popup.click()
    driver.switch_to.default_content()

def search_tag(tag):
    driver.get(f'https://www.tiktok.com/tag/{tag}?lang=tr')

if __name__=='__main__':
    start_bot()
    sleep(1)
    login()
    sleep(1)
    destroy_login_captcha()
    sleep(4)
