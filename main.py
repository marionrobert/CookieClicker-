from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes
delay = 5.0  # Initial seconds


chrome_driver_path = r"C:\Users\Utilisateur1\Development\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# cookie = driver.find_element(By.ID, "cookie")
# cookie.click()
#
#
#
# money_cookies = int((driver.find_element(By.ID, "money")).get_attribute("innerText"))
#
#

money_cookies = 99000

all_items = driver.find_elements(By.CSS_SELECTOR, "div#store div")
all_ids_items = [item.get_attribute("id") for item in all_items]
# print(all_ids_items)

store = {}
for id in all_ids_items:
    tag = driver.find_element(By.ID, f"{id}")
    if id == "buyElder Pledge":
        store[id] = int(tag.get_attribute("innerText").split("Puts")[0].split("-")[1].replace(",", "").strip())
    else:
        store[id] = int(tag.get_attribute("innerText").split("\n")[0].split("-")[1].replace(",", "").strip())

print(store)

item_to_buy = ""
# select the most expensive item you can afford
for item, cost in store.items():
    if money_cookies > cost:
        item_to_buy = item

# buy the most expensive



