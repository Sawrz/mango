# Installation

Mango uses PostgreSQL for the database backend. Therefore, follow these instructions carefully.

Install PostgreSQL and the following dependencies: 

```bash
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev python3-dev
```

Enable `postresql.service`:

```bash
sudo systemctl enable --now postgresql.service
```

Use the PostgreSQL superuser 

```bash
sudo -u postgres psql
```

and create the database and database user for Mango:

```postgresql
CREATE DATABASE MANGO_DB;
CREATE USER MANGO_USER WITH ENCRYPTED PASSWORD '<MANGO_USER_PASSWORD>';
ALTER ROLE MANGO_USER SET client_encoding TO 'utf8';
ALTER ROLE MANGO_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE MANGO_USER SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE MANGO_DB TO MANGO_USER;
```

Replace `MANGO_DB`, `MANGO_USER`, and `MANGO_USER_PASSWORD` with the values you prefer.

Exit PostreSQL with `\q`, and copy `mango/example.env` to `mango/.env`

```bash
cp mango/example.env mango/.env
```

and set the following mandatory values:

- `SECRET_KEY`: The Key for your Django instance (never share that key)
- `DB_NAME`: The value you set instead of `MANGO_DB`
- `DB_USER`: The value you set instead of `MANGO_USER`
- `DB_PASSWORD`: The value you set instead of `MANGO_USER_PASSWORD`

In addition, you can set your Email credentials, so you get an Email if somebody uses the contacts page.

Finally, install Mangos dependencies, make the DB migrations and copy the static files:

```bash
make install
```
