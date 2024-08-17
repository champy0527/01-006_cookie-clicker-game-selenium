from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

assert "Cookie Clicker" in driver.title

# ------------------ COOKIE ------------------ #

start_time = time.time()
end_time = start_time + (5 * 60)
store_check = time.time()

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")


while True:
    cookie.click()
    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))  # keep track of the money

    if time.time() > store_check + 5:

        # get the divs that are available, meaning starts with #buy and the class is empty
        store_divs = driver.find_elements(By.XPATH, "//*[starts-with(@id, 'buy') and @class='']")
        available_to_click = store_divs[::-1]  # reverse the list of store_divs we found

        # debugger to see items
        store_items = [item.text for item in available_to_click]
        print(store_items)

        print(money)

        if available_to_click:
            available_to_click[0].click()

        store_check = time.time()

    if time.time() >= end_time:
        print(f"Your ending money is: {money}")
        print(f"Your cookies per second rate is: {driver.find_element(By.ID, "cps").text}")
        break

time.sleep(2)
driver.quit()
