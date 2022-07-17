import sys
import datetime
import json
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import xlsxwriter

def main_funtion():
  test_list =[]
  test_list1= []
  
  res = []
  for o in range(2):  
    urlo= "https://github.com/spinnaker/front50/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    reqo= requests.get(urlo)
    soupo= BeautifulSoup(reqso.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/front50/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(2):  
    urlkw= "https://github.com/spinnaker/echo/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    reqskw= requests.get(urlkw)
    soupo = BeautifulSoup(reqskw.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/echo/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(1):  
    urlkh= "https://github.com/spinnaker/halyard/pulls?q=label%3Atarget-release%2F1.28+is%3Aclosed+"
    reqskh= requests.get(urlkh)
    soupo = BeautifulSoup(reqskh.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/halyard/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(1):  
    urlkw= "https://github.com/spinnaker/keel/pulls?q=label%3Atarget-release%2F1.28+is%3Aclosed+"
    reqskw= requests.get(urlkw)
    soupo = BeautifulSoup(reqskw.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/keel/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(1):  
    urlke= "https://github.com/spinnaker/keel/pulls?q=label%3Atarget-release%2F1.28+is%3Aclosed+"
    reqske= requests.get(urlke)
    soupo = BeautifulSoup(reqske.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/keel/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(1):  
    urlk= "https://github.com/spinnaker/kayenta/pulls?q=label%3Atarget-release%2F1.28+is%3Aclosed+"
    reqsk= requests.get(urlk)
    soupo = BeautifulSoup(reqsk.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/kayenta/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(2):  
    urlf= "https://github.com/spinnaker/fiat/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    reqsf= requests.get(urlf)
    soupo = BeautifulSoup(reqsf.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/fiat/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(3):  
    urlr= "https://github.com/spinnaker/rosco/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    reqsr= requests.get(urlr)
    soupo = BeautifulSoup(reqsr.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/rosco/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(2):  
    urld= "https://github.com/spinnaker/igor/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    reqsi= requests.get(urld)
    soupo = BeautifulSoup(reqsi.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/igor/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(10):  
    urld= "https://github.com/spinnaker/deck/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    print(urld)
    reqso= requests.get(urld)
    soupo = BeautifulSoup(reqso.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/deck/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
  for o in range(3):  
    urlo= "https://github.com/spinnaker/orca/pulls?page="+str(o+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    print(urlo)
    reqso= requests.get(urlo)
    soupo = BeautifulSoup(reqso.text, 'html.parser')

    for link in soupo.find_all('a'):
        if link.get('href').startswith("/spinnaker/orca/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for l in test_list1:
        if l not in res:
            res.append(l)
    print(test_list1)
  
  for d in range(2):  
    url1= "https://github.com/spinnaker/gate/pulls?page="+str(d+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    #print(url1)
    reqs1= requests.get(url1)
    soup1 = BeautifulSoup(reqs1.text, 'html.parser')

    for link in soup1.find_all('a'):
        if link.get('href').startswith("/spinnaker/gate/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list1.append("https://github.com" + link.get('href'))

    for p in test_list1:
        if p not in res:
            res.append(p)
    print(test_list1)
  for k in range(6):  
    url= "https://github.com/spinnaker/clouddriver/pulls?page="+str(k+1)+"&q=label%3Atarget-release%2F1.28+is%3Aclosed"
    #print(url)
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.find_all('a'):
        if link.get('href').startswith("/spinnaker/clouddriver/pull/") and not link.get('href').endswith("partial-pull-merging"):
            test_list.append("https://github.com" + link.get('href'))

    for i in test_list:
        if i not in res:
            res.append(i)
  
  gitDataStore(res)
    

def gitDataStore(data1):    
    try:
        dataLen=0
        #workbook  = xlsxwriter.Workbook('target-release/1.28.xlsx')
        #sheet = workbook.add_worksheet()
        your_workbook = Workbook() 
        sheet = your_workbook.active
        for i in range(len(data1)):
            sheet["A{}".format(dataLen+i+1)] = data1[i]
        your_workbook.save(filename="test3.xlsx")
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
