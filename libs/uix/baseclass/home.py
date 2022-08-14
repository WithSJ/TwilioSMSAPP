from ast import Pass
from kivymd.uix.list import  ImageLeftWidget
from kivymd.uix.screen import MDScreen 
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from libs.applibs import utils

utils.load_kv("home.kv")

class Home_Screen(MDScreen):
    pass
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass