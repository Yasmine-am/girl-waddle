print("Start api read applicatie")

import requests as r

paginaresultaat = r.get('https://catfact.ninja/facts')

print(paginaresultaat)

feitjes = paginaresultaat.json()

print(feitjes["current_page"])
print(feitjes["data"][0])