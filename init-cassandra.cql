-- Create the keyspace
CREATE KEYSPACE IF NOT EXISTS your_keyspace WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

-- Use the keyspace
USE your_keyspace;

-- Create the table
CREATE TABLE IF NOT EXISTS Products (
  discount_price double,
  timestamp timestamp,
  description text,
  version text,
  title text,
  price double,
  event_original text,
  PRIMARY KEY (timestamp)
);
