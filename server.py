from flask import Flask, request
from libs.applibs import authentication
import datetime
import json

app = Flask(__name__)
#, methods=['POST']
@app.route('/', methods=['POST'])
def result():
    dataDict = authentication.read_json_file("C:\\Twilio\\report.json")
    if dataDict == 0 :
        dataDict = dict()

    data = dict(request.form)
    time = datetime.datetime.now()
    dataDict["DateTime"] = str(time)
    dataDict["TimeStamp"] = time.timestamp()
    dataDict[data["MessageSid"]] = data
    with open("C:\\Twilio\\report.json","a") as jsonFile:
        jsonFile.write(json.dumps(dataDict,indent=4))
    
    # should display 'bar'
    return 'Received !' # response to your request.

app.run(port=5000)