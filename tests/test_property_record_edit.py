from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_page import PropertyPage
from resources.property_explorer_page import PropertyExplorerPage
import time
from faker import Faker
import pytest

@pytest.mark.smoke
def test_property_record_edit(logged_in_chrome: Page):
    logger.info("test property function created")

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    home_page = HomePage(logged_in_chrome)

    home_page.properties_tab.click()
    logger.info("clicked on properties tab")
    time.sleep(3)

    property_page = PropertyPage(logged_in_chrome)

    property_page.properties_new_button.click()
    time.sleep(3)
    logger.info("clicked on properties new button")

    property_page.property_name_fill.click() 
    logger.info("clicked on property's name text box")
    
    fake = Faker()

    random_name = fake.first_name()
    property_page.property_name_fill.fill(f"{random_name}-villa") #f string
    logger.info(f"entered {random_name} in property name text box")

    property_page.property_address.click()
    logger.info("clicked on property address text box")

    random_address = fake.address()
    property_page.property_address.fill(f"{random_address}")
    logger.info(f"entered {random_address} in property's address text box")

    property_page.property_state.click()
    logger.info("clikced on property's state text box")
    
    random_state = fake.state()
    property_page.property_state.fill(f"{random_state}")
    logger.info(f"entered {random_state} name in property's state text box")

    property_page.property_zip.click()
    logger.info("clicked on property's zip text box")
    
    random_zip = fake.zipcode()
    property_page.property_zip.fill(f"{random_zip}")
    logger.info(f"entered {random_zip} code in property's zip text box")

    max_scrolls = 3
    scroll_count = 0   # reset for every page

    while scroll_count < max_scrolls:

        print("Scrolling...", scroll_count + 1)

        # Scroll down using mouse wheel
        property_page.page.mouse.wheel(0, 800)
        scroll_count += 1

        print("Scrolling completed")
        logger.info("successfully scrolled the property record page")

    random_bed_number = fake.random_int(min=1 , max=5)
    property_page.property_bed_fill.fill(f"{random_bed_number}")
    logger.info(f"entered {random_bed_number} in property's bed text box")
    time.sleep(2)

    random_bath_number = fake.random_int(min=1 , max=5)
    property_page.property_bath_fill.fill(f"{random_bath_number}")
    logger.info(f"entered {random_bath_number} in property's bath text box")
    time.sleep(2)

    random_asking_price = fake.random_int(min=0, max=1200000 , step=50000)
    property_page.property_asking_price_fill.fill(f"{random_asking_price}")
    logger.info(f"entered {random_asking_price} in property's asking price text box")
    time.sleep(2)

    property_page.property_save_button.click()
    time.sleep(2)
    logger.info("successfully saved property record")

    property_page.property_edit_button.click()
    time.sleep(2)
    logger.info("successfully clicked on property edit button")

    print("Checking Property Name locator...",flush = True)

    print("Locator count:", property_page.property_name_fill.count() , flush = True)
    property_page.property_name_fill_after_edit.clear()
    time.sleep(2)

    logger.info("successfully cleared the existing name")

    random_name = fake.first_name()

    property_page.property_name_fill_after_edit.fill(f"{random_name}-villa") #f string
    time.sleep(2)
    logger.info(f"entered {random_name} in property name text box")

    property_page.property_save_button_after_edit.click()
    time.sleep(2)
    logger.info("successfully saved the record after edit")