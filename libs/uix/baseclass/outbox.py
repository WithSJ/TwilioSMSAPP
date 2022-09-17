import imp
from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList,OneLineListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.snackbar import Snackbar
from libs.applibs import utils,twilio_api
from kivy.clock import Clock
import datetime

utils.load_kv("outbox.kv")

class Outbox_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.INList = list()
        self.ClockRunning = Clock.schedule_interval(self.update_outlist, 1)
        self.SelectedNumber = None
        
       
    
    def on_list_press(self,event):
        self.SelectedNumber = event.text
        self.ids.all_msgs.clear_widgets()
        filedata = utils.read_json_file(utils.UserDataFile)
        if filedata != 0:
            for k in dict(filedata):
                data = filedata[k]
                if data["Number"] == event.text:
                    self.send_msg(data["Message"],data["DateTime"],data["Number"])
                else:
                    continue
        
    def filter_list(self,text):
        self.ids.container.clear_widgets()
        # print(text)    
        for num in self.INList:
            if text in num:
                self.ids.container.add_widget(
                    OneLineListItem(text=num,on_press=self.on_list_press)
                )

    def update_outlist(self,dt):
        filedata = utils.read_json_file(Filename=utils.UserDataFile)
        if filedata != 0:
            for k in dict(filedata):
                if filedata[k]["Number"] not in self.INList:
                    # print(filedata[k]["Number"])
                    self.ids.container.add_widget(
                        OneLineListItem(text=filedata[k]["Number"],on_press=self.on_list_press)
                    )

                    self.INList.append(filedata[k]["Number"])

        



    def chat_textbox(self):
        """
            MDCard size change when MSGbox use multilines.
            MDCard y axis size incress when MSGbox y axis size incress
        """
        fixed_Y_size = self.ids.root_chatroom.size[1]/3
        msg_textbox=self.ids.msg_textbox.size
        
        if msg_textbox[1] <= fixed_Y_size:
            
            self.ids.send_card.size[1]=msg_textbox[1]
            # print(msg_textbox)
        else:
            self.ids.send_card.size[1]=fixed_Y_size

    def click_send_msg(self,msg_data,server_url):
        time = datetime.datetime.now()
        if self.SelectedNumber == None:
            Snackbar(text= "Select Number from List").open()
        elif len(server_url) < 5:
            Snackbar(text= "Server URL Problem.").open()
        else:
            time = datetime.datetime.now()
            utils.ActiveUserData["server_url"] = server_url
            msgRespSid =twilio_api.twilio_send_msg(utils.ActiveUserData,msg_data,self.SelectedNumber)
            # msgRespSid =  twilio_api.twilio_send_msg(utils.ActiveUserData,msg_text,number)
            Report = {
                "DateTime" : str(time),
                "TimeStamp" : time.timestamp(),
                "Number" : self.SelectedNumber,
                "Message" : msg_data,
                "SID" : msgRespSid
            }
            usrdatafile = utils.read_json_file(utils.UserDataFile)
            if usrdatafile == 0 :
                writeData = dict()
                writeData[Report["SID"]] = Report
                
            else:
                usrdatafile[Report["SID"]] = Report
                writeData = usrdatafile
                
            utils.write_json_file(utils.UserDataFile,writeData)
            self.send_msg(msg_data,str(time),self.SelectedNumber)
    

    def send_msg(self,msg_data,time_data,number_data):
        """
            When send button use to send msg this function call
            and clear MSGbox 
        """
        
        text_msg = MDLabel(text=msg_data,halign="left")
        
        sizeX = self.ids.msg_textbox.size[0]    

        sizeY = self.ids.msg_textbox.size[1]+60
        # ->> sizeY is equal to msg_textbox sizeY because text_msg sizeY not work 
        # that's why i use msg_textbox is called 'Jugaad'
        
        
        msg_card= MDCard(
            orientation= "vertical",
            size_hint=[None,None],
            size=[sizeX,300],
            spacing=8,
            padding=20,
            elevation=9,
            ripple_behavior= True,
            radius= [25,25,25,0 ]

        )
        msg_card.add_widget(MDLabel(
            text= f"To :> {number_data} {' '*4} Date&Time :> {time_data}",
            theme_text_color= "Secondary",
            size_hint_y= None,
            height= 50
        ))
        msg_card.add_widget(MDSeparator(
            height= "1dp"
        ))

        msg_card.add_widget(text_msg)
        self.ids.all_msgs.add_widget(msg_card)
        # print(msg_data)
        self.ids.msg_scroll_view.scroll_to(msg_card)
        self.ids.msg_textbox.text=""
    pass
class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass