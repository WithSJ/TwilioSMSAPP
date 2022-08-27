from __future__ import with_statement
from kivymd.uix.screen import MDScreen 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from libs.applibs import utils
import json
utils.load_kv("report.kv")

class Report_Screen(MDScreen):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            pos_hint= {"center_x":0.5, "center_y":0.5},
            use_pagination=True,
            # name column, width column, sorting function column(optional)
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Phone Number", dp(60)),
                ("MessageSid", dp(30)),
                ("DateTime", dp(30)),
                ("Message", dp(30)),
            ]
            
        )

        self.ids.data_table.add_widget(self.data_tables)
        self.load_data_row()

    def load_data_row(self):
        # allData = dict()
        # with open(utils.UserDataFile) as userdata:
        #     with open(utils.ReportDataFile) as reportdata:
        #         udata = json.load(userdata)
        #         for 


        data = (
                    "1",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                    "+918058458276",
                    "message ssid",
                    "17-08-2000 5:45",
                    "Hello world",
                )

        self.data_tables.row_data.append(data)
        

        

class ContentNavigationDrawer(MDBoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass