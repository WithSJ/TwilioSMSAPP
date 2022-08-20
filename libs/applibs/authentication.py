import json
ActiveUserData = dict()

def read_json_file():
    try:
        with open("auth.json") as jsonFile:
            return json.load(jsonFile)
    except:
        return 0

def write_json_file(data:dict):
    with open("auth.json","w") as jsonFile:
        jsonFile.write(json.dumps(data,indent=4))
        
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

    FileData = read_json_file()
    if FileData != 0:
        if username in FileData:
            return False,"Username already taken."
        FileData[username]= DATA
    else:
        FileData= {username : DATA}
    
    write_json_file(FileData)
    return True,"Account created."


    
def login(username,password):
    FileData = read_json_file()
    if FileData != 0:
        if username in FileData:
            if FileData[username]["password"] == password:
                global ActiveUserData
                ActiveUserData = {username:FileData[username]}
                return True,"Successful login."
            else:
                return False,"Wrong password."
        else:
            return False,"User not found."

    else:
        return False,"User not found."
