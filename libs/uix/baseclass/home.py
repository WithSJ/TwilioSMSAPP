from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.clock import Clock
from libs.applibs import utils
from plyer import filechooser
import threading
import datetime
import json
import time


utils.load_kv("home.kv")

class Home_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ListBox = list()
        Clock.schedule_interval(self.update_on_clock, 0.5)
        self.sleepThread = time.sleep

    def update_on_clock(self,dt):
        print("Clock",dt) 
        self.ids.progressbar.value = utils.ProgreassBarValue
        print(utils.ProgreassBarValue)
        if len(self.ListBox) > 0:
            listdata = self.ListBox[0]
            self.ListBox.remove(listdata)
            self.ids.container.add_widget(
                        OneLineListItem(text=listdata)
                    )
        

    def file_manager_open(self):
        self.ids.ser_url.text = utils.ActiveUserData["server_url"]
        filechooser.open_file(on_selection=self.select_path,multiple=True)

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;4
        :param path: path to the selected directory or file;
        '''
        self.path = path
        self.ids.filenamefield.text = ", ".join(path)
    def sendNuberList(self,msg_text):
        Report= dict()
        for selected_file in self.path:
            with open(selected_file) as filedata:
                NumFileData = set(filedata.readlines())
                FileLen = len(NumFileData)
                i = 0
                for number in NumFileData:
                    i+=1
                    number = str(number).removesuffix("\n")
                    time = datetime.datetime.now()
                    Report[number] = {
                        "DateTime" : str(time),
                        "TimeStamp" : time.timestamp(),
                        "Number" : number,
                        "Message" : msg_text
                    }
                    # print(number)
                    self.ListBox.append(number)
                    utils.ProgreassBarValue = (i/FileLen)*100
                    self.sleepThread(.25)

                    
                    
        # print("Active USer",utils.ActiveUserData)
        with open(f"C:\\Twilio\\{utils.ActiveUserData['username']}_report.json","a") as jsonFile:
            jsonFile.write(json.dumps(Report,indent=4))


    def send_to_all(self):
        """Send sms to all phone numbers"""
        print("Send to all clicked")
        msg_text = self.ids.msg_field.text
        th1 = threading.Thread(target= self.sendNuberList,args=(msg_text,))
        th1.start()

        


    
class SideNavMenu(MDNavigationLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ListBox = list()
        self.ClockRuning = Clock.schedule_interval(self.update_on_clock, 0.5)
     
    def update_on_clock(self,dt):
        print("Clock222",dt)
        if "username" in utils.ActiveUserData:
            self.ids.nav_drawer_header.title = utils.ActiveUserData["username"] 
            self.ClockRuning.cancel()
        
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass