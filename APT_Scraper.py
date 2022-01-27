from bs4 import BeautifulSoup
import requests

source = requests.get('https://attack.mitre.org/groups/').text

soup = BeautifulSoup(source, 'lxml')

table = soup.find('tbody')

for row in table.find_all('tr'):
    rowCells = row.find_all('td')
    print('ID: ' + rowCells[0].a.text.strip())
    print('Desc: ' + rowCells[3].text.strip())
    associates = (rowCells[2].text.strip())
    if(associates != ''):
        print('Associates: ' + associates)
    else:
        print('Associates: None')
    print()
