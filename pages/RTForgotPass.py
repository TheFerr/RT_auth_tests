from .base import WebPage
from .elements import WebElement, ManyWebElements

class ForgotPass(WebPage):

    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)

    # input fields поиска
    input_usrname = WebElement(id='username')
    input_passw = WebElement(id="captcha")
    button_further = WebElement(id="reset")
    button_backward = WebElement(id="reset-back")

    err_message = WebElement(id="form-error-message")

    captcha_img = WebElement(class_name="rt-captcha__image")

    tab_phone = WebElement(id="t-btn-tab-phone")
    tab_mail = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_ls = WebElement(id="t-btn-tab-ls")