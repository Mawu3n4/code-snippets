VIRTUALENV="virtualenv"
VIRTUALENV_DIR=env

setup: env deps

env:
	test -d env || ($(VIRTUALENV) -p `which python2.7` $(VIRTUALENV_DIR) || true)
	. $(VIRTUALENV_DIR)/bin/activate

deps:
	pip install -r requirements.txt -t src/lib
