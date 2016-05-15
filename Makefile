# This file is part of django-environments.
# https://github.com/delgiudices/django-environments

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Luis Del Giudice <luis.dg19@gmail.com>

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies (do not forget to create a virtualenv first)
setup:
	pip install flake8
	@pip install -U -e .\[tests\]

# Flake8
lint:
	@flake8 django_environments

# test your application (tests in the tests/ directory)
test: unit lint

unit:
	@coverage run --branch `which nosetests` -vv -s tests/
	@coverage report -m --fail-under=80

# show coverage in html format
coverage-html: unit
	@coverage html

# run tests against all supported python versions
tox:
	@tox

#docs:
	#@cd django_environments/docs && make html && open _build/html/index.html
