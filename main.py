from kivy.core.window import Window
Window.maximize()

from libs.uix.baseclass.chat_room import Chat_Room_Screen
from libs.uix.baseclass.forgot import Forgot_Screen
from libs.uix.baseclass.home import Home_Screen
from libs.uix.baseclass.login import Login_Screen
from libs.uix.baseclass.profile import Profile_Screen
from libs.uix.baseclass.root import Root
from libs.uix.baseclass.signup import Signup_Screen
from libs.uix.baseclass.verification import Verification_Screen
from libs.uix.baseclass.outbox import Outbox_Screen
from libs.uix.baseclass.inbox import Inbox_Screen
from libs.uix.baseclass.report import Report_Screen

from kivymd.app import MDApp

class TwilioSMSApp(MDApp):
    """
    Hamster App start from here this class is root of app.
    in kivy (.kv) file when use app.method_name app is start from here
    """

    def __init__(self, **kwargs):
        super(TwilioSMSApp, self).__init__(**kwargs)
        
        self.APP_NAME = "Twilio SMS App"
        self.COMPANY_NAME = "Develop By Sandeep Jadam"
        
    def chat_room(self,touch,a):
        """Switch to Chatroom. but username and chatroom username 
        change according to which one you touch in chat list"""
        
        name = touch.text
        self.screen_manager.get_screen("chat_room").ids.profile_bar.title = name


        self.screen_manager.change_screen("chat_room")
    

    def build(self):
        """
        This method call before on_start() method so anything
        that need before start application all other method and code 
        write here.
        """
        # self.theme_cls.primary_palette = "Yellow"
        # self.theme_cls.primary_hue = "500"

        #self.theme_cls.accent_palette = "Amber"
        #self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"
    
        self.screen_manager = Root()
        self.screen_manager.add_widget(Login_Screen())
        self.screen_manager.add_widget(Signup_Screen())
        self.screen_manager.add_widget(Forgot_Screen())
        self.screen_manager.add_widget(Verification_Screen())
        self.screen_manager.add_widget(Home_Screen())
        self.screen_manager.add_widget(Chat_Room_Screen())
        self.screen_manager.add_widget(Profile_Screen())
        self.screen_manager.add_widget(Outbox_Screen())
        self.screen_manager.add_widget(Inbox_Screen())
        self.screen_manager.add_widget(Report_Screen())


        return self.screen_manager
    
    def on_start(self):
        """
        Anything we want to run when start application that code is here.
        """
        self.screen_manager.change_screen("login")
        # self.all_chats()

if __name__ == "__main__":
    # Start application from here.
    TwilioSMSApp().run() 
