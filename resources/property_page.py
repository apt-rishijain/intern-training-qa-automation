from resources.BasePage import BasePage
from playwright.sync_api import Page 

class PropertyPage(BasePage):
    def __init__(self , page : Page) -> None:
        super().__init__(page) 

    @property
    def property_name_label(self):
        return self.page.locator("//span[@title='Property Name']")

    @property
    def properties_tab(self):   
        return self.page.locator("//span[normalize-space()='Properties']")    

    @property
    def properties_new_button(self):
        return self.page.locator("//div[@title='New']")

    @property
    def property_name_fill(self):
        return self.page.locator("//input[@type='text' and @name='Name']")

    @property
    def property_name_fill_after_edit(self):
        return self.page.get_by_role("dialog").locator("input[name='Name']")

    @property
    def property_save_button(self):
        return self.page.locator("//button[normalize-space()='Save']")

    @property
    def property_save_button_after_edit(self):
        return self.page.locator("//button[@name='SaveEdit']")

    @property
    def property_bed_fill(self):
        return self.page.locator('//input[@name="Beds__c"]')

    @property
    def property_bath_fill(self):
        return self.page.locator('//input[@name="Baths__c"]')

    @property
    def property_asking_price_fill(self):
        return self.page.locator("//input[@name='Price__c' and @inputmode='decimal']")

    @property
    def property_address(self):
        return self.page.locator("//input[@name='Address__c' and @class='slds-input']")

    @property
    def property_state(self):
        return self.page.locator("//input[@name='State__c' and @class='slds-input']")

    @property
    def property_zip(self):
        return self.page.locator("//input[@name='Zip__c' and @class='slds-input']")

    @property
    def property_edit_button(self):
        return self.page.locator("//button[@name='Edit']")

    @property
    def property_record_cancel_button(self):
        return self.page.locator("//button[@name='CancelEdit' and text()='Cancel']")

    @property
    def property_new_record_broker_name_fill(self):
        return self.page.locator("//input[@placeholder='Search Brokers...' and @role='combobox']")

    @property
    def required_name_field_error_text(self):
        return self.page.locator("//div[@part='help-text' and contains(text(), 'Complete this field.')]")

    @property
    def asking_price_exceeding_limit_error_text(self):
        return self.page.locator("//div[@data-name='Price__c' and contains(., 'value outside of valid range')]")

    @property
    def broker_selection_combobox(self):
        return self.page.locator("lightning-base-combobox-item")

    

    

    

   
