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

migrate: ## migrate databases
	$(call make_migrations)

clean: ## cleans migrations and static files folder
	$(call clean_up)

flush: clean ## removes migrations and static files folders in addition to delete the SQLite DB
	rm db.sqlite3

simple_update: ## action after updating mango to make sure everything work as expected
	pip install -r requirements.txt
	$(call make_migrations)
	python3 manage.py collectstatic --noinput

update: simple_update ## action after updating mango to make sure everything work as expected if using gunicorn
	systemctl restart gunicorn.service

deploy: simple_update ## install all dependencies of mango
	python3 manage.py createsuperuser
	python3 manage.py check --deploy
