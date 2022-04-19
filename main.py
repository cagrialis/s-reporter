from excelPy import createExcel, nowTime
import sys

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

with open(sys.argv[1], "r") as file:
    data = file.read().rstrip()

parsed_html = BeautifulSoup(data, "html.parser")

titleArr = []
vulnArr = []
descArr = []

# name of vuln packet
for title in parsed_html.body.find_all('h2', attrs={'class': 'vue--issue-title__title'}):
    titleArr.append(title.findChild("span", recursive=False).text)
# vuln name
for i in parsed_html.body.findAll('small', attrs={'class': 'vue--issue-title__category'}):
    vulnArr.append(i.text)

for title in parsed_html.body.find_all('li', attrs={'class': 'vue--issue-meta-item vue--issue-meta-item-vuln-db'}):
    descArr.append(title.findChild("a", recursive=False).get("href"))

appName = ((parsed_html.body.find('h3', attrs={'class': 'vue--project-page-header-name-format__source'}).text).split())[2]

try:
    createExcel(appName, titleArr, vulnArr, descArr)
    print("Excel file created.")
    print(f"Your excel file is here \"reports/{appName.replace('/','_')}-{nowTime}-snyk-reports.xlsx\"")
except:
    print("Excel file couldn't created.")