import json
def read_json_file():
    try:
        with open("auth.json") as jsonFile:
            return json.load(jsonFile)
    except:
        return 0

def write_json_file(data:dict):
    with open("auth.json","a") as jsonFile:
        jsonFile.write(json.dumps(data,indent=4))
        
def signup(username,password) -> str:
    FileData = read_json_file()
    if FileData != 0:
        if username in FileData:
            return "Username already taken."

    write_json_file({username : password})
    return "Account created."


    
def login(username,password):
    FileData = read_json_file()
    if FileData != 0:
        if username in FileData:
            if FileData[username] == password:
                return "Successful login."
            else:
                return "Wrong password."
        else:
            return "User not found."

    else:
        return "User not found."
