from __future__ import with_statement
import os
from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.clock import Clock
from libs.applibs import utils
import json
utils.load_kv("report.kv")

class Report_Screen(MDScreen):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.load_data_table()
        
        # self.ClockRunning = Clock.schedule_interval(self.update_on_clock, 5)

    
    def load_data_table(self):
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            pos_hint= {"center_x":0.5, "center_y":0.5},
            use_pagination=True,
            # name column, width column, sorting function column(optional)
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("To_Phone", dp(30)),
                ("From_Phone", dp(30)),
                ("Message_Sid", dp(80)),
                ("Date_Time", dp(50)),
                ("Account_Sid", dp(80))
            ]
            
        )

        self.load_data_row()
        self.ids.data_table.add_widget(self.data_tables)
   
    def clear_report(self):
        os.remove(utils.ReportDataFile)
        os.remove(utils.UserDataFile)
        
    def load_data_row(self):
        # allData = dict()
        # with open(utils.UserDataFile) as userdata:
        #     with open(utils.ReportDataFile) as reportdata:
        #         udata = json.load(userdata)
        #         for 
        reportData = utils.read_json_file(Filename=utils.ReportDataFile)
        num = int()
        if reportData != 0:
            for key_data,val_data in list(dict(reportData).items())[::-1]:
                num +=1
                smsStatusIcon = None
                if dict(val_data).get("SmsStatus") == "delivered":
                    smsStatusIcon= "checkbox-marked-circle",[39 / 256, 174 / 256, 96 / 256, 1]
                elif dict(val_data).get("SmsStatus") == "sent":
                    smsStatusIcon= "alert", [255 / 256, 165 / 256, 0, 1]
                else:
                    smsStatusIcon= "alert-circle", [1, 0, 0, 1]


                data = (
                            str(num),
                            # dict(val_data).get("SmsStatus"),
                            (smsStatusIcon[0], smsStatusIcon[1], dict(val_data).get("SmsStatus")),
                            dict(val_data).get("To"),
                            dict(val_data).get("From"),
                            dict(val_data).get("MessageSid"),
                            dict(val_data).get("DateTime"),
                            dict(val_data).get("AccountSid")
                        )

                self.data_tables.row_data.append(data)
        


        
        
    def update_on_clock(self,dt):
        # print("Not Report")
        if utils.StartReport:
            # print("-----------YEs Report")
            self.load_data_row()
            utils.StartReport = False
            
            self.ClockRunning.cancel()

        

class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass