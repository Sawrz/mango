modules=core blog contact portfolio

define make_migrations
	for path in $(modules); do \
		python3 manage.py makemigrations $$path; \
	done
	python3 manage.py migrate
endef

define clean_up
	for path in $(modules); do \
  		rm -rf $$path/migrations \
  		rm -rf $$path/__pycache__; \
	done
	rm -rf staticfiles
endef

install-packages: ## installs requirements
	pip install -r requirements.txt

migrate: ## migrate databases
	$(call make_migrations)

clean: ## cleans migrations and static files folder
	$(call clean_up)

flush: clean ## removes migrations and static files folders in addition to delete the SQLite DB
	rm db.sqlite3

update: migrate ## migrate and collect static assets
	python3 manage.py collectstatic --noinput

deploy: update ## deploy mango
	python3 manage.py check --deploy

local-deploy: deploy ## deploy mango and create superuser
	python3 manage.py createsuperuser
	python3 manage.py check --deploy
