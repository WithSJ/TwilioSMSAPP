import json
from libs.applibs import utils
from libs.applibs.utils import read_json_file,write_json_file
        
def signup(
    username,password,
    account_sid,auth_token,phone_num) -> str:

    DATA = {
        "username" : username,
        "password" : password,
        "account_sid" : account_sid,
        "auth_token" : auth_token,
        "phone_num" : phone_num
    }

    FileData = read_json_file(utils.AuthDataFile)
    if FileData != 0:
        if username in FileData:
            return False,"Username already taken."
        FileData[username]= DATA
    else:
        FileData= {username : DATA}
    
    write_json_file(Filename=utils.AuthDataFile,data= FileData)
    return True,"Account created."


    
def login(username,password):
    FileData = read_json_file(utils.AuthDataFile)
    if FileData != 0:
        if username in FileData:
            if FileData[username]["password"] == password:
                utils.ActiveUserData = FileData[username]
                return True,"Successful login."
            else:
                return False,"Wrong password."
        else:
            return False,"User not found."

    else:
        return False,"User not found."
