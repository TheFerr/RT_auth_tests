from .base import WebPage
from .elements import WebElement, ManyWebElements

class RegNew(WebPage):

    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)

    input_fname = WebElement(xpath='//input[@name="firstName"]')
    input_lname = WebElement(xpath='//input[@name="lastName"]')
    input_region = WebElement(xpath='//input[@autocomplete="new-password"]')
    # Калмыкия Респ
    input_phone_mail = WebElement(id="address")

    input_new_passw = WebElement(id="password")
    input_passw_confirm = WebElement(id="password-confirm")

    button_reg = WebElement(tag_name="button")

    url_success_reg = 'https://b2c.passport.rt.ru/account_b2c/page?state'
