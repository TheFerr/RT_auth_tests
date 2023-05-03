import pytest
from pages.RTMain import MainPage
from credentials import *
from helpers import get_red_color


@pytest.mark.negative
@pytest.mark.regress
@pytest.mark.auth
@pytest.mark.parametrize("usr, paswd", \
                         [(valid_phone_user, invalid_pass), \
                          (valid_email_user, invalid_pass), \
                          (valid_login_user, invalid_pass), \
                          (valid_ls_user, invalid_pass), \
                          (invalid_phone_user, valid_phone_pass), \
                          (invalid_email_user, valid_email_pass), \
                          (invalid_login_user, valid_login_pass), \
                          (invalid_ls_user, valid_ls_pass)],
                         ids=['PHONE', 'EMAIL', 'LOGIN', 'LS', 'FakePHONE', 'FakeEMAIL', 'FakeLOGIN', 'FakeLS'])
def test_authpage_auth_negative(web_browser, usr, paswd):
    """ Negative auth """

    page = MainPage(web_browser)
    page.wait_page_loaded(timeout=10)

    if usr == valid_ls_user or usr == invalid_ls_user:
        page.tab_ls.click()

    page.input_usrname = usr
    page.input_passw = paswd
    page.button_login.click()

    assert page.form_error_mess.is_presented(), 'Error auth notice is absent'
    assert get_red_color(page.form_error_mess.get_css('color')) > 200, 'Error auth notice is not red'
    assert get_red_color(page.link_forgotpw.get_css('color')) > 200, 'Forgot password link is not red'
