from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time



def run_sel():
    start_time = time()
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_experimental_option("debuggerAddress","localhost:9222")
    options.add_experimental_option("detach", True)
    # options.add_argument(r"--remote-debugging-port=9222")
    # options.add_argument(r"--user-data-dir=C:\Users\f.huseynli_ext\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r"--user-data-dir=C:\Users\f.huseynli_ext\Desktop\store")
    driver = webdriver.Chrome(options=options)
    driver.get("https://adobe.noxtools.com/?")


# title = driver.title
# assert title == "Web form"
# driver.implicitly_wait(1000)

    driver.implicitly_wait(10)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# input_field = driver.find_element(By.CLASS_NAME, "checkout-steps")
# print(input_field)
# input_field2 = driver.find_element(By.CLASS_NAME, "cardholderName")
# print(input_field2)
 # switching to second iframe based on index
# Store iframe web element

    input_field2 = driver.find_element(By.ID, "assetIdr")
    input_field2.send_keys('761328156')

    # button = driver.find_element(By.ID, "checkout-payment-continue") 
    # driver.execute_script("arguments[0].click();", button)
    # button.click()

    # driver.quit()
# run_sel()