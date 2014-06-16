#!/usr/bin/python

import csv
from datetime import datetime, date, time
outHeader = ["melding_id","appuser_id","plaats_id","gemeente_id","subcategorie_code","hoofdcategorie_code","melding_status_id","melding_statusgebruiker_id","melding_statusgebruiker_omschrijving","melder_geslacht","melder_voornaam","melder_achternaam","melder_straat","melder_huisnummer","melder_postcode","melder_plaats","melder_telefoonnummer","melder_email","melder_contact_mail","melder_contact_telefoon","melding_datumtijd","melding_type","melding_position","melding_gemeente","melding_plaats","melding_straat","melding_huisnummer","melding_postcode","melding_locatieomschrijving","melding_omschrijving","melding_hoofdcategorie","melding_subcategorie","melding_aantalbijlagen","melding_verwerking_resultaat","melding_verwerking_afspraak","melding_verwerking_toelichting","melding_verwerking_mail","melding_verwerking_form","melding_verwerking_ws","melding_hash","melding_created","melding_modified","melding_deleted", "bijlage_id"]

appendix = {}
with open('appendix.csv', 'rb') as f:
  appendixReader = csv.DictReader(f)
  for row in appendixReader:
    appendix[row['melding_id']] = row['bijlage_id']

with open('../buitenBeter/reports_m.csv', 'wb') as out:
  with open('../buitenBeter/reports.csv', 'rb') as f:
    writer = csv.DictWriter(out, outHeader, delimiter="|")    
    reader = csv.DictReader(f)
    for row in reader:
      for d in ["melding_datumtijd", "melding_verwerking_mail", "melding_verwerking_form", "melding_verwerking_ws", "melding_created", "melding_modified", "melding_deleted"]:
        if row[d] != "":
          row[d] = datetime.strptime(row[d], "%d.%m.%Y %H:%M")
      row["melding_position"] = "(" + row['melding_longitude'].replace(",",".",1) + ", " + row['melding_latitude'].replace(",",".",1) + ")"
      del row["melding_longitude"]
      del row["melding_latitude"]
      # add appendix id (for images)
      if row['melding_id'] in appendix:
        row["bijlage_id"] = appendix[row['melding_id']]
      # free description of issue
      row["melding_omschrijving"] = row["melding_omschrijving"].replace("\n", "\\n")
      # feedback from municipality
      row["melding_verwerking_toelichting"] = row["melding_verwerking_toelichting"].replace("\n", "\\n")
      
      writer.writerow(row)

