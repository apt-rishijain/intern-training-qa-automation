from resources.BasePage import BasePage
from playwright.sync_api import Page 

class HomePage(BasePage):
    def __init__(self , page : Page) -> None:
        super().__init__(page) 


    @property
    def property_explorer_tab(self):
        return self.page.locator("//span[normalize-space()='Property Explorer']")

    @property
    def contacts_tab(self):
        return self.page.locator("//span[normalize-space()='Contacts']")

    @property
    def brokers_tab(self):
        return self.page.locator("//span[normalize-space()='Brokers']")

    @property
    def properties_tab(self):   
        return self.page.locator("//a[contains(@href, '/lightning/o/Property__c/home')]//span[text()='Properties']")

    @property
    def property_name_label(self):
        return self.page.locator("//span[@title='Property Name']")       

    @property
    def broker_name_label(self):
        return self.page.locator("//span[@title='Broker Name']")    

    @property
    def contacts_name_label(self):
        return self.page.locator("//span[@title='Name']")    

    @property
    def property_explorer_name_label(self):
        return self.page.locator ("//h1[normalize-space()='Property Explorer']")

    