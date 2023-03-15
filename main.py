from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

run_time = time.time_ns() + 300 * 10**9  # 5 minute run
delay = 5.0  # Initial seconds


chrome_driver_path = r"C:\Users\Utilisateur1\Development\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
cookie.click()



def get_money_cookies():
    return int((driver.find_element(By.ID, "money")).get_attribute("innerText"))


# def get_store():
store = {}
all_items_names = ["Elder Pledge", "Time machine", "Portal", "Alchemy lab", "Shipment", "Mine", "Factory", "Grandma", "Cursor"]
for item in all_items_names:
    tag = driver.find_element(By.ID, f"buy{item}")
    if item == "Elder Pledge":
        store[item] = int(tag.get_attribute("innerText").split("Puts")[0].split("-")[1].replace(",", "").strip())
    else:
        store[item] = int(tag.get_attribute("innerText").split("\n")[0].split("-")[1].replace(",", "").strip())
print(store)

# while run_time > time.time_ns():
#     cookie.click()