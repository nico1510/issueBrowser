#!/usr/bin/python

import csv
import json

categories = {}
with open('categories.csv', 'rb') as f:
  categoriesReader = csv.DictReader(f, fieldnames=["name","description","code"])
  for row in categoriesReader:
    categories[row['code']] = row["name"] + "<br/>" + row["description"]
  print json.dumps(categories);

appendix = {}
with open('appendix.csv', 'rb') as f:
  appendixReader = csv.DictReader(f)
  for row in appendixReader:
    appendix[row['melding_id']] = row['bijlage_id']


with open('reports.csv', 'rb') as f:
  reader = csv.DictReader(f)
  for row in reader:
    code = "L.marker(["
    code += row['melding_latitude'].replace(",",".",1)
    code += "," + row['melding_longitude'].replace(",",".",1)
    code += "]).addTo(map).bindPopup('"
    code += row['melding_datumtijd'] + '<br/>'
    if row['hoofdcategorie_code'] != '':
      code += categories[row['hoofdcategorie_code']]
    if(row['melding_aantalbijlagen'] != "0" and appendix.has_key(row['melding_id'])):
      src = row['melding_datumtijd'][4] + "/" + row['melding_id'] + "/" + row['melding_id'] + "_" + appendix[row['melding_id']] + '.jpg'     
      code += '<br/><img src="buitenBeter/' + src + '" width="250" />'
    code += "');"
    print code
