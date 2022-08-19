from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

from libs.applibs import utils
from plyer import filechooser
utils.load_kv("home.kv")

class Home_Screen(MDScreen):

    def file_manager_open(self):
        filechooser.open_file(on_selection=self.select_path,multiple=True)

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;4
        :param path: path to the selected directory or file;
        '''
        self.path = path
        self.ids.filenamefield.text = ", ".join(path)

    def send_to_all(self):
        """Send sms to all phone numbers"""
        print("Send to all clicked")
        for selected_file in self.path:
            with open(selected_file) as filedata:
                for number in filedata.readlines():
                    print(str(number).removesuffix("\n"))


    
    
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass