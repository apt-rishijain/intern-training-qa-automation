
from playwright.sync_api import Locator, Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> str:
        return self.page.title()

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text().strip()

    def wait_for_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()

    def wait_for_url(self, pattern: str) -> None:
        self.page.wait_for_url(pattern)

    def get_url(self) -> str:
        return self.page.url

    def go(self, url: str) -> None:
        self.page.goto(url)

    def set_slider(self, locator: Locator, value: int) -> None:
        locator.fill(str(value))
        expect(locator).to_have_value(str(value))    
