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

Exit PostgreSQL with `\q`, and copy `mango/example.env` to `mango/.env`

```bash
cp mango/example.env mango/.env
```

and set the following mandatory values:

- `SECRET_KEY`: The Key for your Django instance (never share that key)
- `DB_NAME`: The value you set instead of `MANGO_DB`
- `DB_USER`: The value you set instead of `MANGO_USER`
- `DB_PASSWORD`: The value you set instead of `MANGO_USER_PASSWORD`
- `ALLOWED_HOSTS`: The domain for your site
- `DEBUG`: Should be `False` in production environments.

In addition, you can set your Email credentials, so you get an Email if somebody uses the contacts page.

Install Mangos dependencies, make the DB migrations and copy the static files:

```bash
make deploy
```

Finally, start the site, e.g., `python3 manage.py runserver`, and navigate to `<URL>/admin`. Log in with your
credentials, navigate to `Users`, and select your username. Fill in your credentials and hit save. 

# Resources

- [Using PostgreSQL with Django](https://djangocentral.com/using-postgresql-with-django/)
- [How To Deploy Django App with Nginx, Gunicorn, PostgreSQL and Let’s Encrypt SSL on Ubuntu](https://djangocentral.com/deploy-django-with-nginx-gunicorn-postgresql-and-lets-encrypt-ssl-on-ubuntu/)
- [Using Environment Variables In Django](https://djangocentral.com/environment-variables-in-django/)
