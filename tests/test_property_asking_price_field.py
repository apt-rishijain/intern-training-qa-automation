from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_page import PropertyPage
import time
from faker import Faker
import pytest

@pytest.mark.smoke
def test_property_asking_price_field(logged_in_chrome: Page):
    logger.info("test property function created")
    
    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")
    
    home_page = HomePage(logged_in_chrome)

    home_page.properties_tab.click()
    logger.info("clicked on properties tab")
    time.sleep(2)

    property_page = PropertyPage(logged_in_chrome)

    fake = Faker()
    
    property_page.properties_new_button.click()
    time.sleep(2)
    logger.info("clicked on properties new button")

    random_name = fake.first_name()
    property_page.property_name_fill.fill(f"{random_name}-villa") #f string
    logger.info(f"entered {random_name} in property name text box")

    max_scrolls = 3
    scroll_count = 0  

    while scroll_count < max_scrolls:

        print("Scrolling...", scroll_count + 1)

        # Scroll down using mouse wheel
        property_page.page.mouse.wheel(0, 800)
        scroll_count += 1

        print("Scrolling completed")
        logger.info("successfully scrolled the property record page")

    random_asking_price = fake.random_int(min=100000000, max=120000000, step=50000)
    property_page.property_asking_price_fill.fill(f"{random_asking_price}")
    logger.info(f"entered {random_asking_price} in property's asking price text box")
    time.sleep(2)

    property_page.property_save_button.click()
    time.sleep(2) 
    logger.info("clicked on property save button")   

    assert property_page.asking_price_exceeding_limit_error_text.is_visible(), "exceeding limit price get saved"
    
    


    
    

