from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import random

class SwagBot:
    def __init__(self, username, pw):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.pw = pw
        self.driver.get("https://www.swagbucks.com/p/login")
        sleep(2)
        self.driver.find_element("xpath", "//input[@name=\"emailAddress\"]").send_keys(username)
        self.driver.find_element("xpath", "//input[@name=\"password\"]").send_keys(pw)
        sleep(2)
        self.driver.find_element("xpath", '//button[@id="loginBtn"]').click()
        print( "Sleeping..." )
        sleep(15) # time for you to do the thing that proves you are not a bot
        print( "Done." )

    def survey(self):
        self.driver.find_element("xpath", "/html/body/div[3]/div[1]/header/nav/div[1]/ul/li[2]/a").click()
        sleep(2)
        for i in range(1000):
            x = random.randint(1,2)
            y = random.randint(1,4)
            sleep(y)
            self.driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/span[2]").click()
            sleep(x)
            string1 = "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/span[" + str(x) + "]"
            
            self.driver.find_element("xpath", string1).click()
            sleep(y)
            #self.driver.find_element("xpath", '//button[@class=surveyDashboardCTA sbCta sbBgPrimaryColor"]')
            self.driver.find_element("xpath", "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/button").click()
            #self.driver.find_elements_by_class_name("surveyDashboardCTA sbCta sbBgPrimaryColor").click()
            sleep(x)
            print(i)
            
my_bot = SwagBot( "Your username" , "Your password" )
my_bot.survey()
