from resources.BasePage import BasePage
from playwright.sync_api import Page 

class ContactsPage(BasePage):
    def __init__(self , page : Page) -> None:
        super().__init__(page) 

    @property
    def contact_name_label(self):
        return self.page.locator("//span[@title='Name']")
    
    @property
    def contact_tab(self):
        return self.page.locator("//span[@class='slds-truncate'][normalize-space()='Contacts']")

    @property
    def contact_new_button(self):
        return self.page.locator("//button[@name='NewContact' and text()='New']")

    @property
    def salutation_droplist(self):
        return self.page.locator("//button[@name='salutation' and @role='combobox']")

    @property
    def contact_first_name_fill(self):
        return self.page.locator("//input[@name='firstName']")

    @property
    def contact_last_name_fill(self):
        return self.page.locator("//input[@name='lastName']")

    @property
    def contact_save_button(self):
        return self.page.locator("//button[normalize-space()='Save']")

    @property
    def salutation_options(self):
       return self.page.get_by_role("option")

    