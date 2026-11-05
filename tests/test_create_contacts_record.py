from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.contacts_page import ContactsPage
import time
from faker import Faker
import random
import pytest

@pytest.mark.smoke
def test_create_contacts_record(logged_in_chrome: Page):

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    home_page = HomePage(logged_in_chrome)

    home_page.contacts_tab.click()
    logger.info("clicked on contacts tab")
    time.sleep(2)

    contacts_page = ContactsPage(logged_in_chrome)

        
    contacts_page.contact_new_button.click()
    time.sleep(2)
    logger.info("Clicked on contacts new button")

 
        
    fake = Faker()

    contacts_page.salutation_droplist.click()
    logger.info("clicked on contact record salutation droplist")

    contacts_page.salutation_options.first.wait_for(state="visible")
    options = contacts_page.salutation_options
    random_index = random.randrange(options.count())
    random_option = options.nth(random_index)
    logger.info(f"{random_option}from salutation droplist selected")

    print("Selected Salutation:", random_option.inner_text())
    logger.info("printed selected salutation successfully")
    random_option.click()
    time.sleep(2)

    contacts_page.contact_first_name_fill.click()  
    logger.info("clicked on contacts first name text box") 
    random_first_name = fake.first_name()
    contacts_page.contact_first_name_fill.fill(f"{random_first_name}")
    logger.info(f"entered{random_first_name} as first name in contact's first name text box")
    time.sleep(2)

    random_last_name = fake.last_name()
    contacts_page.contact_last_name_fill.fill(f"{random_last_name}")
    logger.info(f"entered {random_last_name} as last name in contact's last name text box")
    time.sleep(2)

