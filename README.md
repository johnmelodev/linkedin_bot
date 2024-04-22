# LinkedIn Bot

This project is a LinkedIn bot designed to automate the process of adding connections. It is implemented using Python and leverages the Selenium library among others.

## Description

The bot navigates through LinkedIn pages, identifies potential connections based on specified criteria, and sends connection requests along with a custom message.

## Code Explanation

```python
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
```
The above lines import the necessary libraries. Selenium is used for web automation, while other libraries provide support for handling exceptions, interacting with the operating system, and introducing delays.

The `start_driver()` function initializes the Selenium WebDriver with the necessary options and returns the driver and a WebDriverWait object.

The `automate_linkedin_connections(job)` function is the main function that automates the LinkedIn connection process. It starts by logging into LinkedIn using the provided username and password. It then navigates to a specific LinkedIn search page.

The function then enters a loop where it scrolls through the page, identifies 'Connect' buttons, and clicks on them. For each potential connection, it retrieves the contact's name, composes a custom message, and sends the connection request.

If there are no more 'Connect' buttons on the current page, the bot navigates to the next page and continues the process. If it reaches the last page, it prints a message and closes the driver.

The function is invoked at the end with a specific job parameter.

```python
automate_linkedin_connections("Python")
```

## Note

Please replace `'youremail'` and `'yourpassword'` with your actual LinkedIn email and password. Also, ensure that the ChromeDriver version is compatible with your Chrome browser version.

## Dependencies

- Python
- Selenium
- ChromeDriver

## Usage

Run the script in a Python environment. The bot will start adding connections based on the specified criteria. Please ensure you comply with LinkedIn's user agreement when using this bot.