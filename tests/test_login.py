from playwright.sync_api import Page
from base_test import base_test_login
import pytest

@pytest.mark.smoke
def test_login(logged_in_chrome: Page):
   base_test_login(logged_in_chrome)

   