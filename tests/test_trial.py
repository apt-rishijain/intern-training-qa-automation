from base_test import base_test_login, test_create_broker_record
from resources.home_page import HomePage
from playwright.sync_api import Page
from utils.logger import logger
from resources.broker_page import BrokerPage
from resources.property_page import PropertyPage
import time
from faker import Faker
import pytest

def test_trial(logged_in_chrome: Page):
    logger.info("test function created")

    test_create_broker_record(logged_in_chrome)
    logger.info("broker record created")


    

    

    