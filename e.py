import sys
import datetime
import json
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import xlsxwriter

def main_funtion():
    try:
        gitPapulateData()
    except Exception as e:
        print("Exception occurred while processing: ", e)

url = 'https://github.com/spinnaker/clouddriver/pulls?q=is%3Apr+is%3Aclosed+label%3Atarget-release%2F1.28'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

test_list =[]
for link in soup.find_all('a'):
    if link.get('href').startswith("/spinnaker/clouddriver/pull/") and not link.get('href').endswith("partial-pull-merging"):
        test_list.append("https://github.com" + link.get('href'))

res = []
for i in test_list:
    if i not in res:
        res.append(i)
        print(i)

def gitDataStore(data1):    
    try:
        dataLen=0    
        print(dataLen)
        your_workbook = Workbook() 
        sheet = your_workbook.active
        for i in range(len(data1)+dataLen):
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
