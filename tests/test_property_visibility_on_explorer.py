from base_test import base_test_login , base_test_create_property_record ,  get_filtered_property_count
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_explorer_page import PropertyExplorerPage
import time
import pytest

'''creating a property record and checking whether it is visible on explorer page or not'''

@pytest.mark.smoke
def test_property_visibility_on_explorer(logged_in_chrome: Page):
    logger.info("test property function created")

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    property_data = base_test_create_property_record(logged_in_chrome)

    random_property_name = property_data["property_name"]
    random_asking_price = property_data["asking_price"]
    random_bath_number = property_data["bath_number"]
    random_bed_number = property_data["bed_number"]

    home_page = HomePage(logged_in_chrome)

    home_page.property_explorer_tab.click()
    time.sleep(2)
    logger.info("successfully clicked on property explorer tab")
    
    property_explorer_page = PropertyExplorerPage(logged_in_chrome)

    property_explorer_page.search_key.click()
    logger.info("clicked on search key text box on property explorer page")

    property_explorer_page.search_key.fill(random_property_name)
    time.sleep(2)

    logger.info (f"entered the property name {random_property_name} ")

    property_explorer_page.set_slider(property_explorer_page.max_price_slider , random_asking_price)
    time.sleep(2)
    logger.info(f"set the slider at the price of {random_asking_price}")

    property_explorer_page.set_slider(property_explorer_page.bath_num_slider , random_bath_number)
    time.sleep(2)
    logger.info(f"set the slider at the number of bathroom equals to {random_bath_number}")
    
    property_explorer_page.set_slider(property_explorer_page.bed_num_slider , random_bed_number)
    time.sleep(2)
    logger.info(f"set the slider at the number of bedroom equals to {random_bed_number}")

    name = property_explorer_page.property_card_heading(f"{random_property_name}")

    if name.is_visible():
        print("property found")
        logger.info("printing property found as property get visible on property explorer")

    else:
        for i in range(3):
            logged_in_chrome.reload()
            time.sleep(2)
            logger.info("reloading the page as property was not found")

            property_explorer_page = PropertyExplorerPage(logged_in_chrome)

            property_explorer_page.search_key.fill(random_property_name)
            time.sleep(2)
            logger.info("again enetered the name after reloading")

            property_explorer_page.set_slider(property_explorer_page. max_price_slider , random_asking_price)
            time.sleep(2)
            logger.info("again set the price after reloading")

            property_explorer_page.set_slider( property_explorer_page.bath_num_slider, random_bath_number)
            time.sleep(2)
            logger.info("again set the bathroom number after reloading")

            property_explorer_page.set_slider( property_explorer_page.bed_num_slider, random_bed_number)
            time.sleep(2)
            logger.info("again set the bedroom number after reloading")

            # Fetch the locator again after reloading
            name = property_explorer_page.property_card_heading(random_property_name)

            print("Property name searched:", random_property_name)
            print("Matching elements:", name.count())

            if name.is_visible():
                logger.info("Property found on Explorer")
            else:
                logger.error(f"Property {random_property_name} not found on Explorer")
                assert False, "Property not found on Explorer after searching"

            assert name.is_visible() , "property not found on explorer after searching"
            logger.info("property visibility verified")


            assert random_property_name == get_filtered_property_count(random_asking_price , random_bed_number , random_bath_number) ,"Property name didnt match"

    