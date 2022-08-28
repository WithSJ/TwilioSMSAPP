from kivy.lang import Builder
import json,os


ActiveUserData = dict()
ProgreassBarValue = int()
SendMSGThread  = None
ThreadExitEvent = False
ServerThread = None
StartReport = False
UserDataFile = None 
ReportDataFile = "C:\\Twilio\\report.json"
AuthDataFile = "C:\\Twilio\\auth.json"
FolderPath = "C:\Twilio"

def read_json_file(Filename = AuthDataFile ):
    try:
        with open(Filename) as jsonFile:
            return json.load(jsonFile)
    except:
        return 0

def write_json_file(Filename = AuthDataFile,data=dict()):
    with open(Filename,"w") as jsonFile:
        jsonFile.write(json.dumps(data,indent=4))

def load_kv(file_name, file_path=os.path.join("libs", "uix", "kv")):
    """
    `load_kv` func is used to load a .kv file.
    args that you can pass:
        * `file_name`: Name of the kv file.
        * `file_path`: Path to the kv file, it defaults
                       to `project_name/libs/kv`.

    Q: Why a custom `load_kv`?
    A: To avoid some encoding errors.
    """
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())
