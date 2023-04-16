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
  merchant_name VARCHAR(255),
  inactive BOOLEAN
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  category_name VARCHAR(255),
  inactive BOOLEAN
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  tx_value FLOAT,
  merchant VARCHAR(255),
  category VARCHAR(255),
  time_stamp TIMESTAMP,
  user_id INT NOT NULL REFERENCES users(id)
);