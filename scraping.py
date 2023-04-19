print("Start website scrapping applicatie")

import requests as r
from bs4 import BeautifulSoup as b


#print de hele pagina uit
pagina = r.get('https://coinmarketcap.com')
##print(pagina.content)

heeldehtml = b(pagina.content, 'html.parser')
tbody = heeldehtml.find('tbody') #zoeken op element met deze tag
#print(tbody) #print alle tbodies met hun inner html

#print(tbody.prettify()) #print alle tbodies netjes uit

#coins = heeldehtml.find_all('tr') vinden alle elementen

#coins = heeldehtml.find('sc-edc9a476-1 gqomIJ')

for r,rij in coins:
    print(rij)