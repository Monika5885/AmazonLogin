from configparser import ConfigParser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def config():
    config = ConfigParser()
    config.read("Configurations/config.ini")
    return config


@pytest.fixture(scope="class")
def setup(request, config):
    # Set ChromeOptions with anti-bot settings
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Add a realistic user-agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    )

    # Define the Chrome driver service path
    service = Service(r"C:\Users\HP\Desktop\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.get(config.get('Common Info', 'baseurl'))
    request.cls.driver = driver
    yield
    driver.quit()
