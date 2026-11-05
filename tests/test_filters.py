from base_test import base_test_login
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.property_explorer_page import PropertyExplorerPage
import time
import pytest
from pathlib import Path
import json


@pytest.mark.smoke
def test_filters(logged_in_chrome: Page):
    logger.info("test filters function created successfully")

    base_test_login(logged_in_chrome)
    logger.info("logged-in into org successfully")

    home_page = HomePage(logged_in_chrome)

    home_page.property_explorer_tab.click()
    time.sleep(2)
    logger.info("clicked on explorer tab")

    property_explorer_page = PropertyExplorerPage(logged_in_chrome)

    json_path = Path("test_data/filters.json")

    with open(json_path, "r", encoding="utf-8") as file:
      data = json.load(file)

    

    property_explorer_page = PropertyExplorerPage(logged_in_chrome)

    max_price = data[0].get("max_price")

    property_explorer_page.set_slider(property_explorer_page.max_price_slider,max_price )
    logger.info(f"successfully set the slider to {max_price} in max_price slider")
    time.sleep(2)

    bedrooms = data[0].get("bedrooms")

    property_explorer_page.set_slider(property_explorer_page.bed_num_slider , bedrooms)
    time.sleep(2)
    logger.info(f"successfully set the slider to {bedrooms} in bedroom number slider")


    bathrooms = data[0].get("bathrooms")

    property_explorer_page.set_slider(property_explorer_page.bath_num_slider , bathrooms)
    time.sleep(2)
    logger.info(f"successfully set the slider to {bathrooms} in bathroom number slider")


    logger.info("applied filters successfully")

    max_scrolls = 3
    scroll_count = 0   # reset for every page
       
    while scroll_count < max_scrolls:
       
        print("Scrolling...", scroll_count + 1)
       
               # Scroll down using mouse wheel
        property_explorer_page.page.mouse.wheel(0, 800)
        scroll_count += 1

        logger.info("scrolled successfully")

        if property_explorer_page.total_items.is_visible():
            print(property_explorer_page.total_items_number)

    

