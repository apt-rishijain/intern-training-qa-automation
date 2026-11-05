from resources.BasePage import BasePage
from playwright.sync_api import Page 
import re   #regex


class PropertyExplorerPage(BasePage):
    def __init__(self , page : Page) -> None:
        super().__init__(page) 

    @property
    def max_price_slider(self):
        return self.page.locator("//span[normalize-space()='Max Price']/ancestor::lightning-slider//input[@type='range']")      

    @property
    def bath_num_slider(self):
        return self.page.locator("//label[.//span[normalize-space()='Bathrooms']]/following-sibling::div//input[@type='range']")

    @property
    def bed_num_slider(self):
        return self.page.locator("//span[text()='Bedrooms']/ancestor::div[@part='form-element']//input[@type='range']")

  
    # dynamic me property nhilagta

    # def property_card(self, name:str):
    #     return self.page.locator(f"//a[contains(@title,{name})]/descendant::h1")

    
    # def property_card_heading(self, name:str):
    #     return self.property_card(f"//h1[contains({name})]/text()[last()]")

    def property_card(self, name: str):
        return self.page.locator(f"//a[contains(@title, '{name}')]")

    def property_card_heading(self, name: str):
        return self.property_card(name).locator("h1")
    
    @property
    def search_key(self):
        return self.page.locator("//label[contains(., 'Search Key')]/following-sibling::div/input[@part='input']")

    @property
    def total_items(self):
        return self.page.locator("//lightning-layout-item[contains(@class, 'nav-info') and contains(., 'items')]")

    @property
    def total_items_number(self) -> str:
        full_text = self.page.locator("//lightning-layout-item[contains(@class, 'nav-info') and contains(., 'items')]").inner_text()
        match = re.search(r'^\d+', full_text)
        return match 
        
    @property
    def no_items_text_after_search(self):
        return self.page.locator("//lightning-layout-item[contains(., 'items • page')]")



   

   
