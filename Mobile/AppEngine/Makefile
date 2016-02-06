VIRTUALENV="virtualenv"
VIRTUALENV_DIR=env

setup: venv deps

env:
	test -d env || ($(VIRTUALENV) -p `which python2.7` $(VIRTUALENV_DIR) || true)
	. $(VIRTUALENV_DIR)/bin/activate

deps:
	pip install -r requirements.txt
	npm install
