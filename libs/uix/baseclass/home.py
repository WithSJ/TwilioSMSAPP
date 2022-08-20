from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivy.clock import Clock
from libs.applibs import utils
from plyer import filechooser
import threading
import datetime
import json


utils.load_kv("home.kv")

class Home_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

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
    def sendNuberList(self):
        Report= dict()
        for selected_file in self.path:
            with open(selected_file) as filedata:
                for number in set(filedata.readlines()):
                    number = str(number).removesuffix("\n")
                    time = datetime.datetime.now()
                    Report[number] = {
                        "DateTime" : str(time),
                        "TimeStamp" : time.timestamp(),
                        "Number" : number,
                        "Message" : "Your sent msg."
                    }
                    print(number)
        print("Active USer",utils.ActiveUserData)
        with open(f"C:\\Twilio\\{utils.ActiveUserData['username']}_report.json","a") as jsonFile:
            jsonFile.write(json.dumps(Report,indent=4))


    def send_to_all(self):
        """Send sms to all phone numbers"""
        print("Send to all clicked")
        
        th1 = threading.Thread(target= self.sendNuberList)
        th1.start()

        


    
    
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass