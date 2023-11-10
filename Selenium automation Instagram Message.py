from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class instagram:
    def __init__(self,username:str,password:str,people:list=None,msg:str=None):
        self.user= username
        self.password = password
        
        # Setup Firefox options for headless mode
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = False

        # Setup the Firefox Service
        service = Service('C:\drivers\geckodriver-v0.33.0-win64\geckodriver.exe')
        self.driver = webdriver.Firefox(service=service, options=firefox_options)
        self.people = people
        self.msg = msg
        self.url = 'https://www.instagram.com/accounts/login/'
        
        self.login()
        time.sleep(3)
        
        self.popup()
        self.open_msg()
        self.send_msg()
        time.sleep(5)
        
        self.driver.quit()
    
    def web_wait_click(self,xpath):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,xpath))).click()
      
    def login(self):
        """Types the Username and Password for the instagram account to login"""
        
        self.driver.get(self.url)
        username = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME , 'username')))
        username.send_keys(self.user)
        password = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME , 'password')))
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
    
    def popup(self):
        """ Handles the 2 popup that comes after logging into the Account"""
        
        xpath_1 = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"
        xpath_2 = '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
        self.web_wait_click(xpath_1)
        self.web_wait_click(xpath_2)
    
    def open_msg(self):
        message_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div"
        self.web_wait_click(message_xpath)
        
    def send_msg(self):
        for people in self.people:
            # Search for people and send the message
            self.web_wait_click("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div")
            
            input_Xpath = "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input"
            input_name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH ,input_Xpath)))
            input_name.send_keys(people)
            self.web_wait_click("/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div")
            self.web_wait_click("/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div")
            
            message_input = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.xzsf02u')))
            
            for msg in self.msg:
                message_input.send_keys(msg)
            
            message_input.send_keys(Keys.RETURN)
            
if __name__=='__main__':           
    msg = "Hello World"
    people = ["abc","xyz"]
    user = "username"
    password = 'password'
    bot = instagram(user,password,people=people,msg=msg)