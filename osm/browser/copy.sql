
COPY melding FROM '/tmp/reports_m.csv' WITH NULL '' DELIMITER '|';

COPY categories FROM '/tmp/cats.csv' WITH NULL '' DELIMITER ',' CSV QUOTE '"';

set datestyle to 'US';
COPY users FROM '/tmp/user.csv' WITH NULL '\N' DELIMITER ',' CSV QUOTE '"';

COPY (select appuser_id,appuser_title,appuser_name,appuser_username,appuser_pcpassword,appuser_pcpasswordmodified,appuser_pcpasswordvalidity,appuser_pdapassword,appuser_pdapasswordmodified,appuser_pdapasswordvalidity,appuser_street,appuser_streetnumber,appuser_streetpostfix,zip,appuser_city,appuser_phone,appuser_email,appuser_created,appuser_modified,appuser_deleted, '(' || lat || ',' || lon || ')' from zipcodes, users where substring(appuser_zipcode, '^\d*') = zip) to '/tmp/user2';
