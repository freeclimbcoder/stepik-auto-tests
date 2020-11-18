from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла