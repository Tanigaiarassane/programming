from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

'''
	Author: Tanigairassane D
	Purpose: Wrapper routines for creating, accessing and manipulating web \
                 pages using selenium webdriver in different browsers
                 
                 https://magento.com/products/community-edition
'''

def access_ssl():
   #FirefoxProfile profile = new FirefoxProfile();
   #profile.setAssumeUntrustedCertificateIssuer(false);
   #driver = new FirefoxDriver(profile);
   #driver.get("https://google.com")
   pass

def create_driver(name):
    driver = webdriver.Chrome()
    return driver
    
def read_page(driver,url):
	driver.get(url)

def close_driver(driver):
	driver.quit()
	
def select_drop_down(element,option):
	select = Select(element)
        print select.options
	select.select_by_visible_text(option)
    

def locate_element(driver, element, findby):
	''' Locates the elements of a page through different tags
    	    returns the element
	'''

	if findby == "id":
	    elt = driver.find_element_by_id(element)
        elif findby == "name":
            elt = driver.find_element_by_name(element)
        elif findby == "link":
			elt = driver.find_element_by_link_text(element)

	return elt
	
def perform_action(driver,element, action):
       element.click()
	
def shopping_cart(driver):
	read_page(driver,"https://magento.com/products/community-edition")
	element = locate_element(driver, "PRODUCTS","link")
	ActionChains(driver).move_to_element(element).perform()
	time.sleep(2)
	elementq = locate_element(driver, "Enterprise Cloud Edition","link")
        perform_action(driver, elementq, "click")
	#elementq.click()
	
	return 
	
if __name__ == "__main__":
	driver = create_driver("chrome")
        driver.get("https://google.com")

	#shopping_cart(driver)
	#time.sleep(5)
	#close_driver(driver)
	#driver = create_driver("chrome")
	#read_page(driver,"http://the-internet.herokuapp.com/dropdown")
    #element =  locate_element(driver,"dropdown","id")
    #select_drop_down(element, "Option 1")
    #element = locate_element(driver, "lst-ib", "id")
    #element.send_keys("Tanigai")
    #element_submit = locate_element(driver,"btnK","name")
    #element_submit.click()
	    

	
	
