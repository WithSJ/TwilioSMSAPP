from flask import Flask, request
from libs.applibs import utils
import datetime

def TwilioAppServer():
    app = Flask(__name__)
    #, methods=['POST']
    @app.route('/', methods=['POST'])
    def result():
        Report = dict(request.form)
        time = datetime.datetime.now()

        Report["DateTime"] = str(time)
        Report["TimeStamp"] = time.timestamp()
        
        reportdatafile = utils.read_json_file(utils.ReportDataFile)
        if reportdatafile == 0 :
            writeData = dict()
            writeData[Report["MessageSid"]] = Report
            
        else:
            reportdatafile[Report["MessageSid"]] = Report
            writeData = reportdatafile
        
        utils.write_json_file(utils.ReportDataFile,writeData)

        return 'Received !' # response to your request.

    app.run(port=5000)


if __name__ == "__main__":
    TwilioAppServer()