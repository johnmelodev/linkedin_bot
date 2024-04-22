from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def start_driver():
    chrome_options = Options()
    arguments = ['--lang=en', '--window-size=1300,1000']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1
    })

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


def automate_linkedin_connections(job):
    driver, wait = start_driver()
    driver.get('https://www.linkedin.com/login')

    login_field = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='username']")))
    login_field.send_keys('youremail')

    password_field = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@id='password']")))
    password_field.send_keys('yourpassword')

    sign_in_button = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Sign in']")))
    sign_in_button.click()
    sleep(random.randint(3, 6))

    driver.get('https://www.linkedin.com/search/results/people/?activelyHiring="true"&keywords=django&origin=FACETED_SEARCH&page=70&sid=Xjm')
    sleep(3)

    has_next_page = True

    while has_next_page:
        sleep(3)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

        try:
            connect_buttons = wait.until(expected_conditions.visibility_of_all_elements_located(
                (By.XPATH, "//button//span[text()='Connect']")))
        except TimeoutException:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            next_button = wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//span[@class='artdeco-button__text' and text()='Next']")))
            next_button.click()
            continue

        for button in connect_buttons:
            button.click()
            sleep(random.randint(1, 3))

            contact_name = wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//span[@class='flex-1']//strong")))
            contact_name = contact_name.text.split()[0]

            add_note_button = wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Add a note']")))
            add_note_button.click()
            sleep(random.randint(1, 3))

            custom_message = f"Hello {
                contact_name}, Custom message"

            message_field = wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//textarea[@name='message']")))
            message_field.send_keys(custom_message)
            sleep(5)

            send_button = wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Send now']")))
            send_button.click()
            sleep(random.randint(1, 3))

        try:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            next_button = wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//span[@class='artdeco-button__text' and text()='Next']")))
            next_button.click()
            sleep(random.randint(1, 3))
        except Exception as error:
            print('Automation reached the last page')
            has_next_page = False
            driver.close()


automate_linkedin_connections("Python")
