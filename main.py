from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


class GmailLogin:
    def __init__(self, name, password):
        gmail_path = 'https://accounts.google.com/ServiceLogin/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        driver = uc.Chrome(use_subprocess=True)
        driver.get(gmail_path)
        sleep(5)
        driver.find_element(By.ID, 'identifierId').send_keys(name)
        driver.find_element(By.ID, 'identifierNext').click()
        sleep(5)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.ID, 'passwordNext').click()


if __name__ == '__main__':
    name = input('enter your login: ')
    password = input('enter your password: ')
    log = GmailLogin(name, password)


