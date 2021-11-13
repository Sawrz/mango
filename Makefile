modules=main blog contact portfolio resume

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
	rm db.sqlite3

update: ## action after updating mango to make sure everything work as expected
	pip install -r requirements.txt
	$(call make_migrations)
	python3 manage.py collectstatic --noinput

deploy: update ## install all dependencies of mango
	python3 manage.py createsuperuser
	python3 manage.py check --deploy