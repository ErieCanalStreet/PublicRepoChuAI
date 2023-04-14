from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),
                          options=options
                          )

driver.get("https://www.google.com/")

driver.implicitly_wait(3)

noThanks =  driver.find_element(By.CSS_SELECTOR, 'gb_q')

noThanks.click()
