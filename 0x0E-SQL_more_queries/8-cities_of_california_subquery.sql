-- lists all California Cities that can be found in hbtn_0d_usa database
-- lists all rows from cities 
SELECT id, name FROM cities WHERE state_id in (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
