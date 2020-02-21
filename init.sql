CREATE DATABASE aifunddb;
CREATE USER aifunduser WITH PASSWORD 'Nikita123456!';
ALTER ROLE aifunduser SET client_encoding TO 'utf8';
ALTER ROLE aifunduser SET default_transaction_isolation TO 'read committed';
ALTER ROLE aifunduser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE aifunddb TO aifunduser;