CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO customers (name, email) VALUES
  ('testing01', 'tester01@gmail.com'),
  ('testing02', 'tester02@gmail.com');