from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x_element = browser.find_element_by_css_selector("#input_value") 
    x = x_element.text
    y = calc(x)

    x_input = browser.find_element_by_css_selector("input#answer")
    x_input.send_keys(y)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла