# Uncomment to test selenium is running on your system and on which browser(s)

'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def test_chrome_driver():
    service = ChromeService()
    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_edge_driver():
    service = EdgeService()
    driver = webdriver.Edge(service=service)

    driver.quit()


def test_chrome_session():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.quit()


def test_edge_session():
    options = EdgeOptions()
    driver = webdriver.Edge(options=options)

    driver.quit()
'''