from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_explorer_page import PropertyExplorerPage
import time
import pytest

@pytest.mark.smoke
def test_property_explorer(logged_in_chrome: Page):
    logger.info("test explorer function created successfully")

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    home_page = HomePage(logged_in_chrome)

    home_page.property_explorer_tab.click()
    time.sleep(2)
    logger.info("clicked on explorer tab")

    property_explorer_page = PropertyExplorerPage(logged_in_chrome)

    property_explorer_page.set_slider(property_explorer_page.max_price_slider, 600000)
    logger.info("successfully set the slider to 600000 of max price slider")
    time.sleep(2)

    property_explorer_page.set_slider(property_explorer_page.bath_num_slider , 2)
    time.sleep(2)
    logger.info("successfully set the slider to 2 of bathroom number slider")

    property_explorer_page.set_slider(property_explorer_page.bed_num_slider , 3)
    time.sleep(2)
    logger.info("successfully set the slider to 3 of bedroom number slider")

    

    



