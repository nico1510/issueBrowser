
COPY melding FROM '/home/nico/osm/osm/reports_m.csv' WITH NULL '' DELIMITER '|';

COPY categories FROM '/home/nico/osm/osm/categories.csv' WITH NULL '' DELIMITER ',' CSV QUOTE '"';

set datestyle to 'US';
COPY users FROM '/home/nico/osm/osm/userGPS.csv' WITH NULL '\N' DELIMITER E'\t' CSV QUOTE '"';

COPY (select appuser_id,appuser_title,appuser_name,appuser_username,appuser_pcpassword,appuser_pcpasswordmodified,appuser_pcpasswordvalidity,appuser_pdapassword,appuser_pdapasswordmodified,appuser_pdapasswordvalidity,appuser_street,appuser_streetnumber,appuser_streetpostfix,zip,appuser_city,appuser_phone,appuser_email,appuser_created,appuser_modified,appuser_deleted, '(' || lat || ',' || lon || ')' from zipcodes, users where substring(appuser_zipcode, '^\d*') = zip) to '/home/nico/osm/osm/user2';

