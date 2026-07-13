from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.iplt20.com/stats/2026")

wait = WebDriverWait(driver, 20)


try:
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".cookie__accept.cookie__accept_btn")
        )
    ).click()
except:
    pass


view_all = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//a[text()='View All']")
    )
)


driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    view_all
)

time.sleep(2)


driver.execute_script("arguments[0].click();", view_all)


time.sleep(5)

rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

print("Total Rows :", len(rows))

data = []

for row in rows:

    cols = row.find_elements(By.TAG_NAME, "td")

    if len(cols) == 0:
        continue

    row_data = [col.text for col in cols]

    data.append(row_data)

driver.quit()

df = pd.DataFrame(data)

print(df)

df.to_csv("IPL2026.csv", index=False)