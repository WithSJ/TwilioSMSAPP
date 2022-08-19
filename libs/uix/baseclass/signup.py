from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from libs.applibs import utils,authentication

utils.load_kv("signup.kv")

class Signup_Screen(MDScreen):
    def app_signup(
        self,
        username,
        password,
        confirm_password,
        account_sid,
        auth_token,
        phone_num):

        if password.text != confirm_password.text:
            Snackbar(text= "Password not match...").open()
        else:
            msg= authentication.signup(
                username.text,
                password.text,
                account_sid.text,
                auth_token.text,
                phone_num.text)
            
            Snackbar(text= msg[1]).open()