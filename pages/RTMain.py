from .base import WebPage
from .elements import WebElement, ManyWebElements

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru/'


        super().__init__(web_driver, url)

    auth_header = WebElement(class_name="card-container__title")

    # input fields поиска
    input_usrname = WebElement(id='username')
    input_passw = WebElement(id='password')
    button_login = WebElement(id="kc-login")

    form_error_mess = WebElement(id="form-error-message")

    # tabs
    tab_phone = WebElement(id="t-btn-tab-phone")
    tab_mail = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_ls = WebElement(id="t-btn-tab-ls")

    link_forgotpw = WebElement(id="forgot_password")
    link_agreement = WebElement(id="rt-footer-agreement-link")
    link_phone = WebElement(class_name="rt-footer-right__support-phone")
    link_reg = WebElement(id="kc-register")

    # social media OAuth
    # https://oauth.vk.com/
    socm_vk = WebElement(id="oidc_vk")
    # https://connect.ok.ru/
    socm_ok = WebElement(id="oidc_ok")
    # https://connect.mail.ru/oauth/authorize
    socm_mr = WebElement(id="oidc_mail")
    # https://accounts.google.com/o/oauth2
    socm_go = WebElement(id="oidc_google")
    # https://passport.yandex.ru/auth?
    socm_ya = WebElement(id="oidc_ya")

    logo_rt = WebElement(xpath='//*[@class="what-is-container__logo-container"]')
    info_xtra = WebElement(xpath='//h2[@class="what-is__title"]')

    success_auth_head = WebElement(xpath='//h3[@class="card-title"]')
    success_auth_url = 'https://b2c.passport.rt.ru/account_b2c/page'

    url_agreement = 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'
    url_phone = 'tel:88001000800'

    url_vk_start = 'https://oauth.vk.com/authorize'
    url_ok_start = 'https://connect.ok.ru/dk'
    url_mr_start = 'https://connect.mail.ru/oauth/authorize'
    url_go_start = 'https://accounts.google.com/v3/signin/identifier'
    url_ya_start = 'https://passport.yandex.ru/auth'








