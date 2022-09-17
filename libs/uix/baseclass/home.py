from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from libs.applibs import utils,twilio_api
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
        #print("Clock",dt) 
        self.ids.progressbar.value = utils.ProgreassBarValue
        # print(utils.ProgreassBarValue)
        if len(self.ListBox) > 0:
            listdata = self.ListBox[0]
            self.ListBox.remove(listdata)
            self.ids.container.add_widget(
                        OneLineListItem(text=listdata)
                    )
        

    def file_manager_open(self):
        utils.ActiveUserData["server_url"]= self.ids.ser_url.text 
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
                    
                    msgRespSid =  twilio_api.twilio_send_msg(utils.ActiveUserData,msg_text,number)
                    Report = {
                        "DateTime" : str(time),
                        "TimeStamp" : time.timestamp(),
                        "Number" : number,
                        "Message" : msg_text,
                        "SID" : msgRespSid
                    }
                    # print(number)
                    if utils.ThreadExitEvent:
                        exit()
                    

                    
                    self.ListBox.append(number)
                    utils.ProgreassBarValue = (i/FileLen)*100
                    self.sleepThread(.25)

                    
                    
        # print("Active USer",utils.ActiveUserData)
        usrdatafile = utils.read_json_file(utils.UserDataFile)
        if usrdatafile == 0 :
            writeData = dict()
            writeData[Report["SID"]] = Report
            
        else:
            usrdatafile[Report["SID"]] = Report
            writeData = usrdatafile
            
        utils.write_json_file(utils.UserDataFile,writeData)
        # with open(utils.UserDataFile,"a") as jsonFile:
        #     jsonFile.write(json.dumps(Report,indent=4))


    def send_to_all(self):
        """Send sms to all phone numbers"""
        # print("Send to all clicked")
        if len(self.ids.ser_url.text) <= 5:
            Snackbar(text= "Server URL Problem.").open()
        elif len(self.ids.filenamefield.text)<= 3:
            Snackbar(text= "Select Numbers File.").open()
        else:
            utils.ActiveUserData["server_url"]= self.ids.ser_url.text 
            msg_text = self.ids.msg_field.text
            try:
                utils.SendMSGThread.killed = True
                utils.SendMSGThread.join()
            except:
                pass
            finally:
                utils.SendMSGThread = threading.Thread(target= self.sendNuberList,args=(msg_text,))
            
            utils.SendMSGThread.start()

        


    
class SideNavMenu(MDNavigationLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ListBox = list()
        self.ClockRuning = Clock.schedule_interval(self.update_on_clock, 0.5)
     
    def update_on_clock(self,dt):
        # print("Clock222",dt)
        if "username" in utils.ActiveUserData:
            self.ids.nav_drawer_header.title = utils.ActiveUserData["username"] 
            self.ClockRuning.cancel()
        
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass