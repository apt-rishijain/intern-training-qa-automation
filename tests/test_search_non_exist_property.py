from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_explorer_page import PropertyExplorerPage
import time
import pytest

'''searching non existing property in search key on property explorer'''
@pytest.mark.smoke
def test_search_non_exist_property(logged_in_chrome: Page):
    logger.info("test property function created")
    
    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")
    
    home_page = HomePage(logged_in_chrome)

    home_page.property_explorer_tab.click()
    time.sleep(2)
    logger.info("clicked on explorer tab")
        
    property_explorer_page = PropertyExplorerPage(logged_in_chrome)  
    
    property_explorer_page.search_key.click()
    time.sleep(2)
    logger.info("clicked on property explorer search key")
    
    property_explorer_page.search_key.fill("xyz")
    time.sleep(2)
    logger.info("searching non existing property in search key")

    assert property_explorer_page.no_items_text_after_search.is_visible() , "showing properties even after searching a non exisiting property"
    time.sleep(2)
  