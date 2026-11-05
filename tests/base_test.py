from utils.logger import logger
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from conftest import AUTH_FILE
from resources.home_page import HomePage
from resources.broker_page import BrokerPage
from resources.contacts_page import ContactsPage
from resources.property_page import PropertyPage
import time
from faker import Faker
import random


HOME_URL = (
    "https://orgfarm-e04209301e-dev-ed.develop.lightning.force.com/"
    "lightning/page/home"
)

def base_test_login(logged_in_chrome: Page):
    page = logged_in_chrome
    
     # Step 1: Open Salesforce Home using saved browser authentication
    page.goto(HOME_URL, wait_until="domcontentloaded", timeout=60000)
    
    # Step 2: Wait for the page to redirect or finish loading
    try:
        page.wait_for_load_state("domcontentloaded", timeout=30000)
    except PlaywrightTimeoutError:
        pass
    
        # Step 3: Give Salesforce time to complete its redirects
    try:
        page.wait_for_url( "**/lightning/**", timeout=30000)
    except PlaywrightTimeoutError:
        pass
    
        # Step 4: Print the current URL for debugging
    current_url = page.url
    print(f"\nCurrent URL: {current_url}")
    
        # Step 5: Check whether Salesforce is requesting authentication
    if (
            "login.salesforce.com" in current_url
            or "/login" in current_url.lower()
            or "verify" in current_url.lower()
        ):
        raise AssertionError(
                "\nSalesforce redirected to an authentication page.\n"
                "The saved browser session may be expired or invalid.\n"
                f"Current URL: {current_url}\n"
                f"Saved state file: {AUTH_FILE}\n"
                "Log in manually, complete MFA, and save a fresh "
                "browser storage state."
            )
    
    # Step 6: Confirm that Salesforce Lightning opened
    assert "/lightning/" in current_url, (
            "Salesforce Home did not open successfully.\n"
            f"Current URL: {current_url}"
        )
    
    # Step 7: Check that the page is not displaying a login form
    
    login_form = page.locator('input[name="username"]')
    
    assert login_form.count() == 0, (
            "Salesforce appears to be showing a login form instead "
            "of the Home page."
        )
    
    print("Salesforce Home opened using the saved browser session.")

def base_test_create_broker_record(logged_in_chrome: Page) -> str:

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
    broker_page.broker_name_fill.fill(f"{random_broker_name}")
    logger.info(f"broker name - {random_broker_name} entered")
    
    broker_page.broker_save_button.click()
    time.sleep(3)
    logger.info("broker record saved successfully")

    return random_broker_name

def base_test_create_contacts_record(logged_in_chrome: Page):

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

def base_test_create_property_record(logged_in_chrome: Page) -> dict:
    logger.info("test property function created")

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

    return {
        "property_name": f"{random_name}-villa",
        "property_address": random_address,
        "asking_price": random_asking_price,
        "bath_number": random_bath_number,
        "bed_number": random_bed_number
    }

def get_filtered_property_count(self, max_price, beds, baths):

    query = f"""
        SELECT Name
        FROM Property__c
        WHERE Price__c <= {max_price}
        AND Beds__c = {beds}
        AND Baths__c = {baths}
    """

    result = self.sf.query(query)

    return [record["Name"] for record in result["records"]]