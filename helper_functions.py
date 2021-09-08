from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import paths_and_classes as pc

driver_helpers_scope=None
def pass_driver(driver_passed):
    global driver_helpers_scope
    driver_helpers_scope=driver_passed

def find_xpath(xpath,name_of_element=None,retry_num=6):
    if not name_of_element:
        name_of_element=xpath
    data=None

    for i in range (0,retry_num):
        try:
            data=driver_helpers_scope.find_element(By.XPATH,xpath)
            if data:
                print(f'found element {name_of_element}. retry num:{i}')
                break
        except Exception as e:
            sleep(1)
            print(f'cant find {name_of_element} trying again attemp no {i+1}')
            # sleep(1)
            pass
    return data
def dummy():
    cap='//*[@id="tiktok-verify-ele"]/div/div[1]/div[2]/div'
    test=find_xpath(cap,'captcha')

