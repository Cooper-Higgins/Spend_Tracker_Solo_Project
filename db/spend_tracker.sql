DROP TABLE transactions;
DROP TABLE users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  dob TIMESTAMP,
  city VARCHAR(255),
  email VARCHAR(255),
  budget FLOAT
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  tx_value FLOAT,
  merchant VARCHAR(255),
  category VARCHAR(255),
  time_stamp TIMESTAMP
);