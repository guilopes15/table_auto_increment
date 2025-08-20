from functools import partial
from time import sleep

from selenium.webdriver.common.by import By


def send_data(driver, data: list):
    find_id = partial(driver.find_element, by=By.ID)

    name_box = find_id(value='name')
    name_box.send_keys(data[0])
    sleep(0.5)

    quantity_box = find_id(value='quantity')
    quantity_box.send_keys(data[1])
    sleep(0.5)

    description_box = find_id(value='description')
    description_box.send_keys(data[2])
    sleep(0.5)

    button = find_id(value='send')
    button.click()
    sleep(0.5)

    name_box.clear()
    quantity_box.clear()
    description_box.clear()
