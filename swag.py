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
        self.driver.find_element_by_xpath("//input[@name=\"emailAddress\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath('//button[@id="loginBtn"]').click()
        sleep(100) # time for you to do the thing that proves you are not a bot

    def survey(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/surveys')]").click()
        sleep(2)
        for i in range(1000):
            x = random.randint(1,2)
            y = random.randint(1,4)
            sleep(y)
            self.driver.find_element_by_class_name("surveyDropdownVal").click()
            sleep(x)
            string1 = "/html/body/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/span[" + str(x) + "]"
            self.driver.find_element_by_xpath(string1).click()
            sleep(y)
            #self.driver.find_element_by_xpath('//button[@class=surveyDashboardCTA sbCta sbBgPrimaryColor"]')
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/button").click()
            #self.driver.find_elements_by_class_name("surveyDashboardCTA sbCta sbBgPrimaryColor").click()
            sleep(x)
            print(i)
            
my_bot = SwagBot(*your username*, *your password*)
my_bot.survey()
