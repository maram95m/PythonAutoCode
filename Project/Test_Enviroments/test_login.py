import pytest 
from selenium import webdriver
from Pages.Login import LoginPage
from configparser import ConfigParser

      
# config = configparser.ConfigParser()
# config.read('../config.ini')
# url_login = config.get('url','url_login')
# url_Employee = config.get('url','url_Employee')


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.ini", help="Config file path")

@pytest.fixture
def driver(request):
        # Set up the WebDriver (you can use other drivers like Chrome or Firefox)
    config_path = request.config.getoption("--config")
    config = ConfigParser()
    config.read(config_path)

    # Get the browser name from the config file
    browser_name = config.get("browser", "browser")

    # Set up the WebDriver based on the browser name
    if browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
        # driver = webdriver.Chrome()
   
   

    # Open the login page
    return config
    driver.get('http://213.6.2.228/Login')
    yield driver
    
    driver.quit()
   

# def load_config(filename="config.ini"):
#     config = configparser.ConfigParser()
#     config.read("../Config/config.ini")
#     return config 
    
def test_login_valid_credentials(driver,config):
   Login_page = LoginPage(driver)
   Login_page.wait_for_login_page_to_load()
   # perform the login here with valid pararmenters
#    config = load_config()
   username = config.get("credentials","username")
   password = config.get('credentials','password')
      

   Login_page.login(username,password)
   
   assert driver.current_url ==  'http://213.6.2.228/Employee'
   
   
def test_login_invalid_username_credentials(driver,config):
    
    Login_page =LoginPage(driver)
    Login_page.wait_for_login_page_to_load() 
    # config = load_config()
    ivalidusername = config.get('credentials','Invalidusername')
    validpassword = config.get('credentials','validpassword')

    Login_page.login(ivalidusername,validpassword,config)
    
    
    error_message = driver.find_element_by_id("error-message").text
    assert "Invalid username or password" in error_message
   
   
def test_login_invalid_password_credentials(driver,config):
    
    Login_page =LoginPage(driver)
    Login_page.wait_for_login_page_to_load()
    # config = load_config()
    validusername = config.get('credentials','validusername')
    invalidpassword = config.get('credentials','Invalidpassword')

    Login_page.login(validusername,invalidpassword)
    
    
    error_message = driver.find_element_by_id("error-message").text
    assert "Invalid username or password" in error_message
   


# def test_check_browser_type(driver):
#     if isinstance(driver, webdriver.Chrome):
#         print("This test is running on Chrome.")
#     elif isinstance(driver, webdriver.Firefox):
#         print("This test is running on Firefox.")
#     else:
#         print("This test is running on a different browser.")