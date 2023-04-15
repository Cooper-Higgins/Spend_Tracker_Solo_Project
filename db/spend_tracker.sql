DROP TABLE transactions;
DROP TABLE users;
DROP TABLE categories;
DROP TABLE merchants;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  dob DATE,
  city VARCHAR(255),
  email VARCHAR(255),
  budget FLOAT
);

CREATE TABLE merchants (
  id SERIAL PRIMARY KEY,
  merchant VARCHAR(255)
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255)
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  tx_value FLOAT,
  merchant VARCHAR(255),
  category VARCHAR(255),
  time_stamp TIMESTAMP,
  user_id INT NOT NULL REFERENCES users(id)
);