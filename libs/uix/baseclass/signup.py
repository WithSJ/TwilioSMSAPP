from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from libs.applibs import utils,authentication

utils.load_kv("signup.kv")

class Signup_Screen(MDScreen):
    def app_signup(self,username,password,confirm_password):
        if password.text != confirm_password.text:
            Snackbar(text= "Password not match...").open()
        else:
            msg= authentication.signup(username.text,password.text)
            Snackbar(text= msg[1]).open()