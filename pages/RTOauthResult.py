from .base import WebPage
from .elements import WebElement, ManyWebElements

class OauthResult(WebPage):

    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)

    uri = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/first-broker-login'
    caption = WebElement(tag_name="p")
    button_reg = WebElement(tag_name="button")
