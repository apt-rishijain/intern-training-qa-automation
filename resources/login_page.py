from resources.BasePage import BasePage
from playwright.sync_api import Page 

class LoginPage(BasePage) : #LoginPage(child class) inherits the functions of BasePage(parent class)
    def __init__(self , page : Page) -> None:  # init is Special method that initializes the object, self Refers to the current LoginPage object.
       super().__init__(page) #super() → gives access to the parent class, BasePageand .__init__(page) → calls the constructor of BasePage and passes the browser page to it

    @property
    def username(self):
        return self.page.locator("//input[@id='username']")    

    @property
    def password(self) :
        return self.page.locator("//input[@id='password']")

    @property
    def loginbutton(self):
        return self.page.locator("//input[@id='Login']")

     
