from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

cookie = driver.find_element(By.ID, "cookie")
all_items_tags = driver.find_elements(By.CSS_SELECTOR, "div#store div")
all_ids_items = [item.get_attribute("id") for item in all_items_tags]
store = {}
for id_item in all_ids_items:
    store[id_item] = 0


while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        money_cookies = int((driver.find_element(By.ID, "money")).get_attribute("innerText").replace(",", ""))

        for id_item in all_ids_items:
            tag = driver.find_element(By.ID, f"{id_item}")
            if id_item == "buyElder Pledge":
                store.update({id_item: int(tag.get_attribute("innerText").split("Puts")[0].split("-")[1].replace(",", "").strip())})
            else:
                store.update({id_item: int(tag.get_attribute("innerText").split("\n")[0].split("-")[1].replace(",", "").strip())})

        id_item_to_buy = ""
        for item, cost in store.items():
            if money_cookies > cost:
                id_item_to_buy = item

        # buy the most expensive
        driver.find_element(By.ID, f"{id_item_to_buy}").click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 8

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").get_attribute("innerText")
        print(cookie_per_s)
        break