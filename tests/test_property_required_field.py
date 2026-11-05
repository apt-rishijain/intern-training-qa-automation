from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_page import PropertyPage
import time
import pytest


'''TESTING REQUIRED FIELD OF PROPERTY RECORD BY KEEPING IT BLANK '''

@pytest.mark.smoke
def test_property_required_field(logged_in_chrome: Page):
    logger.info("test property function created")
    
    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")
    
    home_page = HomePage(logged_in_chrome)

    home_page.properties_tab.click()
    logger.info("clicked on properties tab")
    time.sleep(2)

    property_page = PropertyPage(logged_in_chrome)
    
    property_page.properties_new_button.click()
    time.sleep(2)
    logger.info("clicked on properties new button")

    property_page.property_save_button.click()
    time.sleep(2) 
    
    assert property_page.required_name_field_error_text.is_visible(), "Required name field error was not displayed"

    
    



    