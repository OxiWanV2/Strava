from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
import os

with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

username = config_data["username"]
password = config_data["password"]
athlete_id = config_data["athlete_id"]

driver = webdriver.Chrome()

driver.get("https://www.strava.com/login")

time.sleep(3)

username_field = driver.find_element("name", "email")
username_field.send_keys(username)

password_field = driver.find_element("name", "password")
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

if "dashboard" not in driver.current_url:
    driver.quit()
    print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ")
    print("Connexion impossible")
    quit()
else:
    print("Connexion réussie", username)

time.sleep(2)

athlete_url = f"https://www.strava.com/athletes/{athlete_id}"
driver.get(athlete_url)

time.sleep(5)

kudo_buttons = driver.find_elements("xpath", "//button[@data-testid='kudos_button']")

for button in kudo_buttons:
    if "active" not in button.get_attribute("class"):
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        print("Le kudo a bien été donnés !")
        time.sleep(2)

print("Tout les kudos on deja été donnés !")

time.sleep(3)

driver.quit()