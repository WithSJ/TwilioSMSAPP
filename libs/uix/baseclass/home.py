from ast import Pass
from kivymd.uix.list import  ImageLeftWidget
from kivymd.uix.screen import MDScreen 
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.filemanager import MDFileManager

from libs.applibs import utils

utils.load_kv("home.kv")

class Home_Screen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            md_bg_color= "#e7e4c0")
    
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
    
    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        self.exit_manager()
        self.ids.filenamefield.text = path
    
    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass