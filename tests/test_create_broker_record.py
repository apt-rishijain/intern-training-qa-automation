from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.broker_page import BrokerPage
import time
from faker import Faker
import pytest

@pytest.mark.smoke
def test_create_broker_record(logged_in_chrome: Page):

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    home_page = HomePage(logged_in_chrome)

    home_page.brokers_tab.click()
    logger.info("clicked on broker tab")
    
    time.sleep(3)

    broker_page = BrokerPage(logged_in_chrome)
    
    broker_page.broker_new_button.click()
    time.sleep(3)
    logger.info("Clicked on broker new button")
    
    broker_page.broker_name_fill.click() 
    logger.info("Clicked on broker name box")
    
    fake = Faker()
    
    random_broker_name = fake.first_name()
    broker_page.broker_name_fill.fill(f"{random_broker_name}-br")
    logger.info(f"broker name - {random_broker_name} entered")
    
    broker_page.broker_save_button.click()
    time.sleep(3)
    logger.info("broker record saved successfully")

   

    






    