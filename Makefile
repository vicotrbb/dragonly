# VARIABLES
ROOT:=./
VENV_BIN_DIR:="venv/bin"

PIP:="$(VENV_BIN_DIR)/pip"
TEST:="$(VENV_BIN_DIR)/pytest"
LOCAL:="$(VENV_BIN_DIR)/gunicorn"

VIRTUALENV:=$(shell which virtualenv)
REQUIREMENTS:="requirements.txt"

APP_NAME=Dragonly

CORE_DIR="/core"
WEB_DIR="/web"

# PHONY

.PHONY: help venv

# UTILS

help:
	@echo "#####################--HELP--#####################"

clean:
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	@find . -type d -name .pytest_cache -delete
	@rm -rf venv

# DEVELOPMENT

define create-venv
virtualenv venv -p python3
endef

venv:
	$(create-venv)
	@$(PIP) install --no-cache-dir -r $(REQUIREMENTS) | grep -v 'already satisfied' || true
