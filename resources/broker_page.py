from resources.BasePage import BasePage
from playwright.sync_api import Page 

class BrokerPage(BasePage):
    def __init__(self , page : Page) -> None:
        super().__init__(page) 

    @property
    def broker_name_label(self):
        return self.page.locator("//span[@title='Broker Name']")

    @property
    def broker_tab(self):   
        return self.page.locator("//a[@title='Brokers']")    

    @property
    def broker_new_button(self):
        return self.page.locator("//div[@title='New']")

    @property
    def broker_name_fill(self):
        return self.page.locator("//input[@type='text' and @name='Name']")

    @property
    def broker_save_button(self):
        return self.page.locator("//button[normalize-space()='Save']")

    @property
    def broker_related_tab(self):
        return self.page.locator("//li[contains(@class, 'slds-tabs_default__item') and @title='Related']")

    @property
    def broker_property_new_button(self):
        return self.page.locator("//button[contains(@class, 'slds-button') and @name='New']")

    @property
    def broker_search_box(self):
        return self.page.locator("//input[@name='Broker-search-input']")

    def broker_after_search_list(self, random_broker_name):
        return self.page.locator(f"//a[@title='{random_broker_name}' and contains(@class, 'slds-truncate')]")

    def property_name_in_broker_related_tab(self , random_property_name):
        return self.page.locator(f"(//span[contains(text(),'{random_property_name}')])")

        