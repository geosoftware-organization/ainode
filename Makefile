ROOT_DIR:=./
SRC_DIR:=./src
REQUIREMENTS_DIR:="requirements"

venv: .venv/bin/activate

venv/bin/activate: requirements.txt
	virtualenv venv
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

migrations:
	python manage.py makemigrations
	python manage.py migrate

run: migrations
	python manage.py runserver

run_all:
	make migrations
	make run

test:
  #TODO
