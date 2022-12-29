import pickle
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os.path

driver = webdriver.Chrome('Tls/chromedriver.exe')


def firstTime(username, password):
    time.sleep(6)
    cookieBtn = driver.find_element(By.XPATH,
                                    "//*[@id='artdeco-global-alert-container']/div/section/div/div[2]/button[1]")
    cookieBtn.click()
    time.sleep(2)
    usernameInput = driver.find_element(By.NAME, "session_key")
    usernameInput.send_keys(username)
    passwordInput = driver.find_element(By.NAME, "session_password")
    passwordInput.send_keys(password)
    time.sleep(5)
    loginBtn = driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/button")
    loginBtn.click()
    pickle.dump(driver.get_cookies(), open("Tls/cookies.pkl", "wb"))


def cookieLoad():
    cookies = pickle.load(open("Tls/cookies.pkl", "rb"))
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.get("https://www.linkedin.com/company/91642186/admin/")


def postArticle(title, article):
    firstPostBtn = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[3]/div[2]/div[1]/div[3]/div/div[2]/main/div/div[1]/div/div[1]/button')
    firstPostBtn.click()
    time.sleep(2)
    textArea = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')
    textArea.click()
    textArea.send_keys(title)
    textArea.send_keys(Keys.ENTER)
    textArea.send_keys(article)
    time.sleep(2)
    submitBtn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
    submitBtn.click()


def fullScript(username, password, title, article):
    driver.get("https://www.linkedin.com")
    time.sleep(5)
    file_exists = os.path.exists('Tls/cookies.pkl')
    if file_exists:
        cookieLoad()
    else:
        firstTime(username, password)
    time.sleep(5)
    postArticle(title, article)
    time.sleep(100000)


