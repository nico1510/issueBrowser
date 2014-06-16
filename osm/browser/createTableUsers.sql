CREATE TABLE users (
appuser_id  integer,
appuser_title  text,
appuser_name  text,
appuser_username  text,
appuser_pcpassword  text,
appuser_pcpasswordmodified  text,
appuser_pcpasswordvalidity  text,
appuser_pdapassword  text,
appuser_pdapasswordmodified  text,
appuser_pdapasswordvalidity  text,
appuser_street  text,
appuser_streetnumber  text,
appuser_streetpostfix  text,
appuser_zipcode  integer,
appuser_city  text,
appuser_phone  text,
appuser_email  text,
appuser_created  timestamp,
appuser_modified  timestamp,
appuser_deleted  timestamp,
user_domicile point
);

ALTER TABLE users ADD PRIMARY KEY (appuser_id);

ALTER TABLE melding ADD CONSTRAINT userfk FOREIGN KEY (appuser_id) REFERENCES users (appuser_id) MATCH FULL;


