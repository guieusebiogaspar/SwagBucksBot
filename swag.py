from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import random
import pickle


class SwagBot:
    def __init__(self, username, pw):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.get("https://www.swagbucks.com/p/login")
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            self.username = username
            self.pw = pw
            sleep(2)
            self.driver.find_element_by_xpath(
                "//input[@name=\"emailAddress\"]").send_keys(username)
            self.driver.find_element_by_xpath(
                "//input[@name=\"password\"]").send_keys(pw)
            login_btn = self.driver.find_element(By.ID, "loginBtn")
            login_btn.click()
            sleep(5)
            pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
            sleep(5)

    def startSurvey(self):
        self.driver.get("https://www.swagbucks.com/surveys")
        sleep(2)
        try:
            while True:
                x = random.randint(1, 2)
                y = random.randint(1, 4)
                sleep(y)
                dropDown = self.driver.find_elements(
                    By.CSS_SELECTOR, (".surveyDropdownVal")
                )
                if(len(dropDown) > 0):
                    dropDown[0].click()
                else:
                    print("Dropdown not found! Trying in 5 mins")
                    sleep(300)
                    self.driver.refresh()
                    continue
                sleep(x)

                options = self.driver.find_elements(By.CSS_SELECTOR, (
                    ".questionDropdownOptions > span")
                )

                random.choice(options).click()

                sleep(x)

                self.driver.find_element(By.CSS_SELECTOR, (
                    ".surveyDashboardCTA")
                ).click()

                sleep(x)
        except Exception as e:
            print(e)
            print("Will try later")
            sleep(60 * 60 * 1)


my_bot = SwagBot("midhun.vnadh5732@gmail.com", "pe3&+&k3_$S8CzQ")
my_bot.startSurvey()
