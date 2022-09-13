from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from libs.applibs import utils,authentication

utils.load_kv("login.kv")

class Login_Screen(MDScreen):
    def app_login(self,username,password):
        msg= authentication.login(username.text,password.text)
        if msg[0]:
            utils.UserDataFile = f"C:\\Twilio\\{utils.ActiveUserData['username']}_report.json"
            Snackbar(text= msg[1]).open()
            utils.StartReport = True
        else:
            Snackbar(text= msg[1]).open()
        
        self.ids.password_field.text = ""
        return msg[0]

