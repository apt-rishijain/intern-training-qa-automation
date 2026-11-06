import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


class Config:
    def __init__(self):
        self.baseurl = os.getenv("SF_BASE_URL", "https://login.salesforce.com/?locale=in")
        self.sf_username = os.getenv("SF_USERNAME")
        self.sf_password = os.getenv("SF_PASSWORD")

        if not self.sf_username or not self.sf_password:
            raise RuntimeError(
                "SF_USERNAME / SF_PASSWORD not set — add them to your .env file."
            )

    