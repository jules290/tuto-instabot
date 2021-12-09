from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/Elève/Desktop/projet/ytb tuto code/video/tuto instabot/chromedriver.exe")

sdbUsername = '[your username]'
sdbPassword = '[your password]'

def Start():
    try:
        driver.get("https://www.instagram.com/")
        print("browser was started")

    except:
        print("browser wasn't started")


def Cookies():
    try:
        driver.find_element(By.CLASS_NAME, "bIiDR").click()
        print("cookies were set")

    except:
        print("cookies weren't")


def Login(username, password):
    try:
        cookie = False
        while cookie == False:
            try:
                if driver.find_element(By.NAME, "username"):
                    cookie = True
                    driver.find_element(By.NAME, "username").send_keys(username)
                    driver.find_element(By.NAME, "password").send_keys(password)

                    driver.find_element(By.CLASS_NAME, "IwRSH").click()

                    connect = False
                    while connect == False:
                        try:
                            if driver.find_element(By.CLASS_NAME, "ctQZg"):
                                print("login was executed")
                                connect = True

                        except:
                            pass

            except:
                pass

    except:
        print("login wasn't executed")


def Follow(url):
    driver.get(url)
    try:
        driver.find_element(By.CLASS_NAME, "yZn4P").click()

        follow = False
        while follow == False:
            try:
                if driver.find_element(By.CLASS_NAME, "T0kll"):
                    print("follow was executed")
                    follow = True

            except:
                pass

    except:
        try:
            if driver.find_element(By.CLASS_NAME, "T0kll"):
                print("follow was already executed")
                follow = True

        except:
            print("an error was happened in the following")


def Close():
    driver.close()



Start()
Cookies()
Login(sdbUsername, sdbPassword)
Follow("https://www.instagram.com/instagram/")
Close()