from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from libs.applibs import utils

utils.load_kv("root.kv")

class Root(ScreenManager):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
        self.screen_list = list() #this list have all screen that user switched
        self.dialog = None
    
    def _key_handler(self, instance, key, *args):
        
        if key is 27:
            #in Desktop this key 27 is Esc and in Phone it's Back btn
            self.previous_screen()
            return True
    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)
        self.screen_list.append(self.last_screen)
    def previous_screen(self):
        """
        Switch to previous screen last screen in screen_list
        """
        if len(self.screen_list) > 1 : 
            self.last_screen=self.screen_list.pop()
        else:
            self.last_screen = "login"

        if self.last_screen == "home" or self.last_screen == "login":
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Do you want to exit?",
                    buttons=[
                        MDFlatButton(
                            text="CANCEL",
                            on_release= self.dialog_close
                        ),
                        MDFlatButton(
                            text="Exit",
                            on_release= exit
                        ),
                    ],
                )
            
            self.dialog.open()
        
        else:
            # print(self.screen_list)
            self.transition.direction = "left"
            self.current = self.screen_list[len(self.screen_list)-1]
            
        
        
        
    
    
    def change_screen(self,name):
        """
        Switch Screen using screen name and 
        """
        self.current = name 
        if name not in self.screen_list:
            self.screen_list.append(self.current)
        else:
            self.screen_list.remove(name)
            self.screen_list.append(self.current)
        
        # print(self.screen_list)

        # if name == "home":            
            # MDBottomNavigation not resize there tabs when app stat in android 
            # to resize when switch to home screen 
            # self.get_screen(name).ids.android_tabs.on_resize()