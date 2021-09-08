import cv2
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
from PIL import Image
import helper_functions as hf
import paths_and_classes as pc


def check_chaptcha_and_destroy(driver,captcha_xpath,gap_image_xpath):
    while True:
        captcha = hf.find_xpath(captcha_xpath, 'captcha')
        if captcha:
            take_screen_shot(gap_image_xpath)
            destroy_captcha(driver)
            sleep(4)
        else:
            break


def take_screen_shot(gap_image_xpath):
    print('taking screen_shot')
    sleep(6)
    bg_image = hf.find_xpath(pc.back_ground_image_xpath, 'bg_image', 10)
    if bg_image:
        bg_image.screenshot('img/bg_image.png')
    gap_image = hf.find_xpath(gap_image_xpath, 'gap_image', 1)
    if gap_image:
        gap_image.screenshot('img/gap_image.png')


def destroy_captcha(driver):
    gap_img = cv2.cvtColor(cv2.imread('img/gap_image.png')[0:67, 2:68], cv2.COLOR_RGB2GRAY)
    gap_edge = cv2.Canny(gap_img, 250, 330)

    bg_img = cv2.imread('img/bg_image.png')[60:160, 68:340]
    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_RGB2GRAY)
    bg_edge = cv2.Canny(bg_img, 230, 315)

    results_matching = cv2.matchTemplate(bg_edge, gap_edge, cv2.TM_CCOEFF_NORMED)
    a, s, d, best_location = cv2.minMaxLoc(results_matching)
    amount = best_location[0]
    drag_slider(amount, driver)


def drag_slider(amount, driver):
    amount = amount
    drag_button = hf.find_xpath(pc.drag_button_xpath, 'slider')
    mouse_automator = ActionChains(driver)
    mouse_automator.click_and_hold(drag_button).perform()
    sleep(1)
    mouse_automator.move_by_offset(23, 1).perform()
    sleep(.5)
    mouse_automator.move_by_offset(10, 1).perform()
    sleep(1.3)
    mouse_automator.move_by_offset(12, 1)
    sleep(1)
    mouse_automator.move_by_offset(21, 1)
    sleep(.3)
    mouse_automator.move_by_offset(amount, -1)
    sleep(1)
    # mouse_automator.drag_and_drop_by_offset(drag_button, amount,0 ).perform()
    mouse_automator.release().perform()
    # sleep(1)


if __name__ == '__main__':
    check_chaptcha_and_destroy(driver,pc.captcha_login_xpath,pc.gap_image_login_xpath)
