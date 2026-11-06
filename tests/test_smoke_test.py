from playwright.sync_api import Page
from base_test import base_test_login
from resources.home_page import HomePage
from utils.logger import logger
import time
import pytest

@pytest.mark.smoke
def test_smoke_test(logged_in_chrome: Page):

    base_test_login(logged_in_chrome)

    home_page = HomePage(logged_in_chrome)

    home_page.properties_tab.click()
    logger.info("clicked on properties tab")

    time.sleep(3)
    assert home_page.is_visible(home_page.property_name_label) , "property name label not visible"
    logger.info("property name label found")

    home_page.brokers_tab.click()
    logger.info("clicked on brokers tab")
    time.sleep(3)
    assert home_page.is_visible(home_page.broker_name_label) , "broker name label not visible"
    logger.info("brokers name label found")

    home_page.contacts_tab.click()
    logger.info("clicked on contacts tab")
    time.sleep(3)
    assert home_page.is_visible(home_page.contacts_name_label) , "contacts name label not visible"
    logger.info("contact name label found")

    home_page.property_explorer_tab.click()
    logger.info("clicked on property explorer tab")
    time.sleep(3)
    assert home_page.is_visible(home_page.property_explorer_name_label) , "property explorer name label not visible"
    logger.info("property explorer name label found")
