from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
            if driver.find_element(By.CLASS_NAME, "y3zKF"):
                driver.find_element(By.CLASS_NAME, "y3zKF").click()

                follow = False
                while follow == False:
                    try:
                        if driver.find_element(By.CLASS_NAME, "T0kll"):
                            print("follow was executed")
                            follow = True

                    except:
                        pass

            elif driver.find_element(By.CLASS_NAME, "T0kll"):
                print("follow was already executed")
                follow = True

        except:
            print("an error was happened in the following")


def LikeByUser(url, postsIndex):
    driver.get(url)
    posts = driver.find_elements(By.CLASS_NAME, "_9AhH0")

    for i in postsIndex:
        posts[i].click()

        like = False
        while like == False:
            try:
                if driver.find_elements(By.CLASS_NAME, "fr66n")[0]:
                    driver.find_elements(By.CLASS_NAME, "fr66n")[0].click()
                    print("post was like")
                    driver.find_element(By.CLASS_NAME, "yiMZG").click()
                    like = True

            except:
                pass


def Comment(url, postsIndex, message):
    driver.get(url)
    posts = driver.find_elements(By.CLASS_NAME, "_9AhH0")

    for i in postsIndex:
        posts[i].click()
        
        comment = False
        while comment == False:
            try:
                if driver.find_elements(By.CLASS_NAME, "rrUvL")[1]:
                    driver.find_elements(By.CLASS_NAME, "rrUvL")[1].click()
                    driver.find_element(By.CLASS_NAME, "Ypffh").send_keys(message)
                    driver.find_element(By.CLASS_NAME, "Ypffh").send_keys(Keys.ENTER)
                    print("post was commented")
                    driver.find_element(By.CLASS_NAME, "yiMZG").click()
                    comment = True

            except:
                pass

def Close():
    driver.close()



Start()
Cookies()
Login(sdbUsername, sdbPassword)
Comment("https://www.instagram.com/instagram/", [0], "hey")
# Follow("https://www.instagram.com/instagram/")
# LikeByUser("https://www.instagram.com/instagram/", [0])
#in the array we indicate the indexes of the publications that we want to like, index 0 corresponds to the most recent publication
Close()