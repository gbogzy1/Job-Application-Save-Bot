from selenium.common import exceptions as exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = input("What is your Linkedin email")
PASSWORD = input("What is your linkedin password")

service = Service("/Users/caleb/Desktop/Development/Chrome Driver")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
action_chain = ActionChains(driver=driver)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London"
           "%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
sign_in.click()

email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

submit = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit.click()

job_list =[]
jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")


def easy_apply():
    apply = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div')))
    apply.click()
    try:
        next1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember471"]')))
        next1.click()
    except exceptions.TimeoutException:
        next1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember495"]')))
        next1.click()

    cv = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember505"]')))
    cv.click()


def submit():
    submit1 = driver.find_element(By.XPATH, '//*[@id="ember635"]/span')
    submit1.click()


def save():
    save1 = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save1.click()
    save1.send_keys(Keys.END)


def remove_message_overhead():
    message_dropdown = driver.find_element(By.XPATH, "/html/body/div[6]/aside/div[1]/header/div[3]/button[2]/li-icon")
    message_dropdown.click()
    time.sleep(1)


remove_message_overhead()

driver.maximize_window()
for job in jobs:
    print(job.text)
    job.click()
    time.sleep(1)
    save()
    time.sleep(3)
    try:
        follow = driver.find_element(By.CLASS_NAME, "follow")
        action_chain.move_to_element(follow).click().perform()
    except exceptions.NoSuchElementException or exceptions.ElementClickInterceptedException:
        follow = driver.find_element(By.CLASS_NAME, "artdeco-button__icon")
        action_chain.move_to_element(follow).click().perform()
    print(job.text)
    time.sleep(2)

driver.quit()

