#!/usr/bin/python

import csv

header = ["appuser_id","appuser_title","appuser_name","appuser_username","appuser_pcpassword","appuser_pcpasswordmodified","appuser_pcpasswordvalidity","appuser_pdapassword","appuser_pdapasswordmodified","appuser_pdapasswordvalidity","appuser_street","appuser_streetnumber","appuser_streetpostfix","appuser_zipcode","appuser_city","appuser_phone","appuser_email","appuser_created","appuser_modified","appuser_deleted"]

createTable = "CREATE TABLE melding (\n"
for col in header:
  createTable += col + " "
  if col[-2:] == "id":
    createTable += " integer"
  else:
    createTable += " text"
  createTable += ",\n"
createTable = createTable[:-2]
createTable += "\n);"
print createTable

