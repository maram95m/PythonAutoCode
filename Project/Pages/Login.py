from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
   def __init__(self, driver):

       self.driver =driver
       self.username_input = (By.NAME,'username')
       self.password_input = (By.NAME,'password')
       self.login_button= (By.XPATH,'//*[@id="myform"]/button')
       
   def set_username(self,username):
        self.driver.find_element(*self.username_input).send_keys(username)
        
        
   def set_password(self,password):
          self.driver.find_element(*self.password_input).send_keys(password)
          
    
   def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

   def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

   def wait_for_login_page_to_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        
   