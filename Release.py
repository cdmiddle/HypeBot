from HypeBot import NormalPurchase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Release(NormalPurchase):


    driver = webdriver.Firefox()
    passW = ''
    emailA = ''
    shoe_size = ''
    cvv = ''
    release_date = ''
    product_url = ''

    def __init__(self, password, email, shoesize, cvv, releasedate, producturl):
        super().__init__(password, email, shoesize, cvv, releasedate, producturl)


    def checkout(self):
        cc_radio = Release.find_element('paymentmethod_pidd77c04c1-faf2-4844-9d53-47ec36b17ccc')


