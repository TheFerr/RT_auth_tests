import pytest
from pages.RTMain import MainPage
from pages.RTRegister import RegNew
from time import sleep
from credentials import *
from helpers import get_red_color


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.parametrize("soc_link,url_start", \
                         [(MainPage.socm_vk, MainPage.url_vk_start), \
                          (MainPage.socm_ok, MainPage.url_ok_start), \
                          (MainPage.socm_mr, MainPage.url_mr_start), \
                          (MainPage.socm_go, MainPage.url_go_start), \
                          (MainPage.socm_ya, MainPage.url_ya_start)], \
                         ids=['VK', 'OK', 'MR', 'GO', 'YA'])
def test_authpage_soc_oauth(web_browser, soc_link, url_start):
    """ Social OAuth link is well """
    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)
    soc_link.click()
    page.wait_page_loaded(timeout=10)
    curr_url = page.get_current_url()
    assert curr_url.startswith(url_start), 'Social OAuth link invalid'


@pytest.mark.front
@pytest.mark.positive
def test_authpage_tabs_autoswitch(web_browser):
    """ Tabs autoswitch depends on input """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)

    page.input_usrname = valid_email_user
    page.input_passw.click()

    assert get_red_color(page.tab_mail.get_css('color')) > 200 and \
           get_red_color(page.tab_phone.get_css('color')) < 20

    page.input_usrname = valid_login_user
    page.input_passw.click()

    assert get_red_color(page.tab_login.get_css('color')) > 200 and \
           get_red_color(page.tab_mail.get_css('color')) < 20

    page.input_usrname = valid_ls_user
    page.input_passw.click()

    assert get_red_color(page.tab_ls.get_css('color')) > 200 and \
           get_red_color(page.tab_login.get_css('color')) < 20


@pytest.mark.auth
@pytest.mark.positive
def test_authpage_auth_phone(web_browser):
    """ Positive auth by phone """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=10)

    page.input_usrname = valid_phone_user
    page.input_passw = valid_phone_pass
    page.button_login.click()

    assert 'Учетные' in page.success_auth_head.get_text(), 'LK page did nor find'
    assert success_auth_url in page.get_current_url(), 'Url success auth page did not find '


@pytest.mark.auth
@pytest.mark.positive
def test_authpage_auth_email(web_browser):
    """ Positive auth by email """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=10)

    page.tab_mail.click()
    page.input_usrname = valid_email_user
    page.input_passw = valid_email_pass
    page.button_login.click()

    assert 'Учетные' in page.success_auth_head.get_text(), 'LK page did nor find'
    assert success_auth_url in page.get_current_url(), 'Url success auth page did not find '


@pytest.mark.auth
@pytest.mark.positive
def test_authpage_auth_bylogin(web_browser):
    """ Positive auth by login """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=10)

    page.tab_login.click()
    page.input_usrname = valid_login_user
    page.input_passw = valid_login_pass
    page.button_login.click()

    assert 'Учетные' in page.success_auth_head.get_text(), 'LK page did nor find'
    assert success_auth_url in page.get_current_url(), 'Url success auth page did not find '


@pytest.mark.regress
def test_authpage_link_password_recovery(web_browser):
    """ Password recovery link is well """
    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)
    page.link_forgotpw.click()
    page.wait_page_loaded(timeout=10)
    assert 'Восстановление' in page.auth_header.get_text(), 'Password recovery link invalid'


@pytest.mark.smoke
def test_authpage_open(web_browser):
    """ Make sure main auth page opened rapidly """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=10)

    assert 'Авторизация' in page.auth_header.get_text(), 'Auth form header did not find'
    assert MainPage.url_agreement in page.link_agreement.get_attr('href'), 'Url agreement page incorrect'
    assert MainPage.url_phone in page.link_phone.get_attr('href'), 'Support phone num is incorrect'


@pytest.mark.smoke
def test_authpage_link_sign_up(web_browser):
    """ Password SignUp link is well """
    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)
    page.link_reg.click()
    page.wait_page_loaded(timeout=10)
    assert 'Регистрация' in page.auth_header.get_text(), 'Sign Up link invalid'


@pytest.mark.regress
def test_authpage_link_agreement(web_browser):
    """ Password SignUp link is well """
    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)
    page.link_agreement.click()
    page.wait_page_loaded(timeout=10)

    assert 'Публичная оферта' in page.auth_header.get_text(), 'Agreement link invalid'


@pytest.mark.smoke
def test_authpage_form(web_browser):
    """ Authpage contains all form elements """
    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)

    assert page.tab_login.is_presented(), 'There is no tab login'
    assert page.tab_mail.is_presented(), 'There is no tab mail'
    assert page.tab_ls.is_presented(), 'There is no tab login'
    assert page.input_passw.is_presented(), 'There is no password field'
    assert page.input_usrname.is_presented(), 'There is no username field'
    assert page.button_login.is_presented(), 'There is no login button'
    assert page.link_forgotpw.is_presented(), 'There is no ling forgot passw'


@pytest.mark.regress
def test_authpage_logo(web_browser):
    """ Authpage contains logo"""

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)

    assert page.info_xtra.is_presented(), 'There is no Extra User Info'
    assert page.logo_rt.is_presented(), 'There is no logo'


@pytest.mark.front
@pytest.mark.regress
@pytest.mark.xfail
def test_authpage_tabs_autoswitch_phone_ls(web_browser):
    """ Tabs autoswitch among phone and LS XFAILED """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)

    page.input_usrname = valid_phone_user
    page.input_passw.click()

    assert get_red_color(page.tab_phone.get_css('color')) > 200 and \
           get_red_color(page.tab_ls.get_css('color')) < 20

    page.input_usrname = valid_ls_user
    page.input_passw.click()

    assert get_red_color(page.tab_ls.get_css('color')) > 200 and \
           get_red_color(page.tab_phone.get_css('color')) < 20

    page.input_usrname = valid_phone_user
    page.input_passw.click()

    assert get_red_color(page.tab_phone.get_css('color')) > 200 and \
           get_red_color(page.tab_ls.get_css('color')) < 20


@pytest.mark.front
@pytest.mark.regress
def test_auth_page_tab_manual_select(web_browser):
    """ Manual tab switch color """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)

    page.tab_mail.click()
    assert get_red_color(page.tab_mail.get_css('color')) > 200 and \
           get_red_color(page.tab_phone.get_css('color')) < 20

    page.tab_phone.click()
    assert get_red_color(page.tab_phone.get_css('color')) > 200 and \
           get_red_color(page.tab_mail.get_css('color')) < 20

    page.tab_login.click()
    assert get_red_color(page.tab_login.get_css('color')) > 200 and \
           get_red_color(page.tab_phone.get_css('color')) < 20

    page.tab_ls.click()
    assert get_red_color(page.tab_ls.get_css('color')) > 200 and \
           get_red_color(page.tab_login.get_css('color')) < 20

    # text_h1 = web_browser.find_element(By.XPATH, '//h1[@class="offer-title"]').text


@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.reg
def test_signup_new_user_phone(web_browser):
    """ New entry SignUp by phone """
    page = MainPage(web_browser)
    page.link_reg.click()
    page.wait_page_loaded()

    page1 = RegNew(web_browser)
    page1.input_fname = random_first_name
    page1.input_lname = random_last_name
    page1.input_phone_mail = new_phone_user
    page1.input_new_passw = new_phone_pass
    page1.input_passw_confirm = new_phone_pass
    page1.button_reg.click()

    i = 0
    # Wait until code input
    while RegNew.url_success_reg not in page1.get_current_url():
        sleep(1)
        i = i + 1
        if i > 100:
            raise AssertionError('Timeout code input')


@pytest.mark.smoke
@pytest.mark.reg
@pytest.mark.positive
def test_signup_new_user_email(web_browser):
    """ New entry SignUp by E-mail """
    page = MainPage(web_browser)
    page.link_reg.click()
    page.wait_page_loaded()

    page1 = RegNew(web_browser)
    page1.input_fname = random_first_name
    page1.input_lname = random_last_name
    page1.input_phone_mail = new_email_user
    page1.input_new_passw = new_email_pass
    page1.input_passw_confirm = new_email_pass
    page1.button_reg.click()

    i = 0
    # Wait until code input
    while RegNew.url_success_reg not in page1.get_current_url():
        sleep(1)
        i = i + 1
        # if
        if i > 100:
            raise AssertionError('Timeout code input')


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.smoke
def test_authpage_auth_byls(web_browser):
    """ Positive auth by LS """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=10)

    page.tab_ls.click()
    page.input_usrname = valid_ls_user
    page.input_passw = valid_ls_pass
    page.button_login.click()

    assert 'Учетные' in page.success_auth_head.get_text(), 'LK page did nor find'
    assert success_auth_url in page.get_current_url(), 'Url success auth page did not find '


@pytest.mark.positive
@pytest.mark.regress
def test_regpage_logo(web_browser):
    """ RegPage contains logo"""

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=15)
    page.link_reg.click()
    page.wait_page_loaded(timeout=10)

    assert page.logo_rt.is_presented(), 'There is no logo'
