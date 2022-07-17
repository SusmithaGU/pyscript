import requests
from bs4 import BeautifulSoup


url = "https://api.github.com/repos/spinnaker/clouddriver/pulls?q=is%3Apr+is%3Aclosed+label%3Atarget-release%2F1.28"
newurl = "https://www.geeksforgeeks.org/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'html.parser')
for i,tag in enumerate(soup.find_all(('a'),attrs={'class':'Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title'})):
    print(i.get('href'))