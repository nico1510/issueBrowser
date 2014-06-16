DROP TABLE melding;
CREATE TABLE melding (
  melding_id  integer  PRIMARY KEY,
  appuser_id  integer,
  plaats_id  integer,
  gemeente_id  integer,
  subcategorie_code  text,
  hoofdcategorie_code  integer,
  melding_status_id  integer,
  melding_statusgebruiker_id  integer,
  melding_statusgebruiker_omschrijving  text,
  melder_geslacht   char(1),
  melder_voornaam  text,
  melder_achternaam  text,
  melder_straat  text,
  melder_huisnummer  text,
  melder_postcode  text,
  melder_plaats  text,
  melder_telefoonnummer  text,
  melder_email  text,
  melder_contact_mail  text,
  melder_contact_telefoon  text,
  melding_datumtijd  timestamp,
  melding_type  integer,
  melding_position  point,
  melding_gemeente  text,
  melding_plaats  text,
  melding_straat  text,
  melding_huisnummer  text,
  melding_postcode  text,
  melding_locatieomschrijving  text,
  melding_omschrijving  text,
  melding_hoofdcategorie  text,
  melding_subcategorie  text,
  melding_aantalbijlagen  integer,
  melding_verwerking_resultaat  text,
  melding_verwerking_afspraak  text,
  melding_verwerking_toelichting  text,
  melding_verwerking_mail  timestamp,
  melding_verwerking_form  timestamp,
  melding_verwerking_ws  timestamp,
  melding_hash  char(32),
  melding_created  timestamp,
  melding_modified  timestamp,
  melding_deleted  timestamp,
  bijlage_id integer
);
