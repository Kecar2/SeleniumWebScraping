from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

website = 'https://www.resultados-futbol.com/livescore'
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//*[@id="cabecera"]/div[8]/a[1]')
all_matches_button.click()

content = driver.find_element(By.ID, 'livescore-box')

matches = driver.find_elements(By.TAG_NAME, 'tr')

partidos = []
for match in matches:
    partidos.append(match.text)

driver.quit()

#pandas
df = pd.DataFrame({'partidos':partidos})
print(df)
df.to_csv('partidos.csv', index=False)

# tbody/table

