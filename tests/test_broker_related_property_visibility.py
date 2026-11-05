from base_test import base_test_login , base_test_create_broker_record
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.broker_page import BrokerPage
from resources.property_page import PropertyPage
import time
from faker import Faker
import pytest

'''creating a property record and then checking on the it's broker's related tab whether the property is showing or not'''

@pytest.mark.smoke
def test_broker_related_property_visibility(logged_in_chrome: Page):
    logger.info("test property function created")

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    random_broker_name = base_test_create_broker_record(logged_in_chrome)

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

    random_property_name = fake.first_name()
    property_page.property_name_fill.fill(f"{random_property_name}-villa") #f string
    logger.info(f"entered {random_property_name} in property name text box")

    max_scrolls = 3
    scroll_count = 0   # reset for every page

    while scroll_count < max_scrolls:

        print("Scrolling...", scroll_count + 1)

        # Scroll down using mouse wheel
        property_page.page.mouse.wheel(0, 800)
        scroll_count += 1

        print("Scrolling completed")
        logger.info("successfully scrolled the property record page")

    property_page.property_new_record_broker_name_fill.click()
    time.sleep(2)
    logger.info("clicked on selecting broker for property")   

    property_page.property_new_record_broker_name_fill.fill(f"{random_broker_name}")
    time.sleep(2)
    logger.info(f"selecting broker - {random_broker_name}")

    property_page.broker_selection_combobox.nth(1).wait_for(state="visible")
    property_page.broker_selection_combobox.nth(1).click()

    property_page.property_save_button.click()
    time.sleep(2)
    logger.info("clicked on property save button")

    home_page.brokers_tab.click()
    logger.info("clicked on broker tab")

    broker_page = BrokerPage(logged_in_chrome)

    broker_page.broker_search_box.click()
    logger.info("clicked on broker search box")

    broker_page.broker_search_box.fill(f"{random_broker_name}")
    time.sleep(2)
    logger.info(f"searching broker- {random_broker_name} ")

    broker_page.broker_search_box.press("Enter")
    time.sleep(2)
    logger.info("Pressed enter after search")

    first_broker = broker_page.broker_after_search_list(random_broker_name)
    first_broker.wait_for(state="visible")
    first_broker.click()
    logger.info("clicked on broker record")
    time.sleep(2)

    broker_page.page.reload()

    time.sleep(3)

    broker_page.broker_related_tab.first.click()
    time.sleep(2)
    logger.info("clicked on broker related tab")

    full_property_name = f"{random_property_name}-villa"

    assert broker_page.property_name_in_broker_related_tab(full_property_name).is_visible() , "property name not visible"

    



  