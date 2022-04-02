from selenium import webdriver
import pytest

driver=webdriver.Chrome()
def test01():
    driver.get("https://www.facebook.com/login/")
    element1=driver.current_url
    assert element1=="https://www.facebook.com/login/"
def test02():
    driver.get("https://www.facebook.com/login/")
    element1 = driver.current_url
    assert element1 == "https://www.facebook.com/login/"