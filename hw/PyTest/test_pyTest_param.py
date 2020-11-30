import time
import math
import pytest
from selenium import webdriver

def answer():
	return(math.log(int(time.time())))



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('task_num', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, task_num):
    link = f"https://stepik.org/lesson/{task_num}/step/1/"
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_css_selector(".textarea")
    input1.send_keys(str(answer()))
    button_send = browser.find_element_by_css_selector(".submit-submission")
    button_send.click()
    verify = browser.find_element_by_css_selector(".smart-hints__hint")
    assert verify.text == "Correct!"
