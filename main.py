from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

from timer import Timer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

assert "Cookie Clicker" in driver.title

# ------------------ COOKIE ------------------ #

timer = Timer(5, 20)   # sets checking the store @ 5 seconds, and end timer @ 20 seconds
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

while timer.game_is_on(): # while the game start runs from time.time() to just before the end_timer_seconds

    money = int(driver.find_element(By.ID, "money").text)  # keep track of the money

    if timer.game_is_on() is False:  # stops the game if timer is at 20 seconds
        print(f"Your ending money is: {money}")
        break

    cookie.click()  # keep clicking

    timer.counting_down()  # start the countdown

    if timer.is_countdown_zero():  # if the timer running hits 0
        print(money)

        try:
            for i in range(7, -1, -1):  # this is how many shop items are in the store
                store_click_div = driver.find_elements(By.CSS_SELECTOR, "#store>div")
                store_click_div.pop()  # grabs the div you can click but removes the empty one

                store_items = driver.find_elements(By.CSS_SELECTOR, "#store>div>b")  # grabs the cost of the store items
                store = [int(item.text.split()[-1].replace(',', '')) for item in store_items if item.text.split()]

                if money >= store[i]:
                    store_click_div[i].click()

        except StaleElementReferenceException:
            print("Encountered stale element. Continue checking store...")

        timer.reset_timer()



time.sleep(2)
driver.quit()
