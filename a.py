import sys
import datetime
import json
import requests
from openpyxl import Workbook

def main_funtion():
    try:
        gitPapulateData()
    except Exception as e:
        print("Exception occurred while processing: ", e)

def gitPapulateData():
    try:
        URL = "https://api.github.com/repos/spinnaker/clouddriver/pulls?base=master"
        newUrl = "https://api.github.com/repos/spinnaker/clouddriver/pulls?q=is%3Apr+is%3Aclosed+label%3Atarget-release%2F1.28"
        headers = {'Authorization': 'token %s' % api_token}
        urla = "https://github.com/spinnaker/clouddriver/pulls?q=label%3Atarget-release%2F1.28+is%3Aclosed"
        requestDatas = requests.get(url = newUrl)
        requestJsonDatas = json.loads(requestDatas.content)
        print(len(requestJsonDatas))
        for requestJsonData  in requestJsonDatas:
            # print(requestJsonData['id'])
            # print(requestJsonData['url'])
            labelDatas = requestJsonData['labels']
            if labelDatas:
                for labelData in labelDatas:
                    if labelData['name'] == 'target-release/1.28':
                        print(requestJsonData['url'])
    except Exception as e:
      print("Exception occurred while processing the request datas:", e)
      raise e 
def gitDataStore(data1, data2):    
    try:    
        your_workbook = Workbook() 
        sheet = your_workbook.active
        for i in range(len(data1)):
            sheet["A{}".format(i+1)] = data1[i]
        your_workbook.save(filename="test.xlsx")
    except Exception as e:
      print("Exception occurred while processing the request datas:", e)
      raise e 

if __name__ == '__main__':
    n = len(sys.argv)

    if n != 2:
        print(
            "Please pass valid 1 arguments")
        exit(0)
    api_token = sys.argv[1]
    main_funtion()