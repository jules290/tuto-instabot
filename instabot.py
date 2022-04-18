from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/Elève/Desktop/projet/ytb tuto code/video/tuto instabot fr/chromedriver.exe")

def Start():
    try:
        driver.get("https://www.instagram.com")
        print("driver ouvert")

    except:
        print("driver non ouvert")


def Cookies():
    try:
        driver.find_element(By.CLASS_NAME, "bIiDR").click()
        print("cookies acceptés")

    except:
        print("cookies non acceptés")


def Login(username, password):
    try:
        cookies = False
        while cookies == False:
            try:
                if driver.find_element(By.NAME, "username"):
                    driver.find_element(By.NAME, "username").send_keys(username)
                    driver.find_element(By.NAME, "password").send_keys(password)
                    cookies = True

                   
                    driver.find_elements(By.CLASS_NAME, "IwRSH")[1].click()

                    connect = False
                    while connect == False:
                        try:
                            if driver.find_element(By.CLASS_NAME, "ctQZg"):
                                print("connecté")
                                connect = True

                        except:
                            pass

            except:
                pass

    except:
        print("non connecté")


def Follow(url):
    driver.get(url)
    try:
        button = False
        while button == False:
            try:
                if driver.find_element(By.CLASS_NAME, "y3zKF"):
                    driver.find_element(By.CLASS_NAME, "y3zKF").click()

                    follow = False
                    while follow == False:
                        try:
                            if driver.find_element(By.CLASS_NAME, "T0kll"):
                                print("follow executé")
                                follow = True

                        except:
                            pass

                elif driver.find_element(By.CLASS_NAME, "T0kll"):
                    print("follow déja executé")
                    follow = True

            except:
                pass

    except:
        print("une erreur est survenue dans le follow")

def LikeByUser(url, postsIndex):
    driver.get(url)

    posts = False
    while posts == False:
        if driver.find_elements(By.CLASS_NAME, "_9AhH0"):
            posts = driver.find_elements(By.CLASS_NAME, "_9AhH0")

            for i in postsIndex:
                posts[i].click()

                like = False
                while like == False:
                    try:
                        if driver.find_elements(By.CLASS_NAME, "fr66n")[0]:
                            driver.find_elements(By.CLASS_NAME, "fr66n")[0].click()
                            print("post liké")
                            driver.find_element(By.CLASS_NAME, "NOTWr").click()
                            like = True

                    except:
                        pass


def Comment(url, postsIndex, message):
    driver.get(url)

    posts = False
    while posts == False:
        if driver.find_elements(By.CLASS_NAME, "_9AhH0"):
            posts = driver.find_elements(By.CLASS_NAME, "_9AhH0")

            for i in postsIndex:
                posts[i].click()

                comment = False
                while comment == False:
                    try:
                        if driver.find_elements(By.CLASS_NAME, "rrUvL")[0]:
                            driver.find_elements(By.CLASS_NAME, "rrUvL")[0].click()
                            driver.find_element(By.CLASS_NAME, "Ypffh").send_keys(message)
                            driver.find_element(By.CLASS_NAME, "Ypffh").send_keys(Keys.ENTER)
                            print("post commenté")
                            driver.find_element(By.CLASS_NAME, "NOTWr").click()
                            comment = True

                    except:
                        pass

Start()
Cookies()
Login("[your mail]", "[your password]")
Follow("https://www.instagram.com/instagram")
# LikeByUser("https://www.instagram.com/instagram", [1])
# Comment("https://www.instagram.com/instagram", [0], "hey")
driver.close()
