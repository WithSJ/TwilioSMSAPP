from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from libs.applibs import utils,authentication

utils.load_kv("login.kv")

class Login_Screen(MDScreen):
    def app_login(self,username,password):
        msg= authentication.login(username.text,password.text)
        Snackbar(text= msg[1]).open()
        return msg[0]

