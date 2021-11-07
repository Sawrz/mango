pip install -r ../requirements.txt
bash migrations.sh
python3 ../manage.py collectstatic --noinput