#!/usr/bin/env bash

# Variables
COLLECTIONS_DIR := ./collections

# Targets
# ------------------------------------------------------------------------------

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Build

venv: ## Creates the python virtual environment
	python3 -m venv venv
	venv/bin/pip install --upgrade pip setuptools wheel
	venv/bin/pip install -r requirements.txt

.PHONY: colls_dir
colls_dir: ## Creates the ansible collections directory
	@mkdir -p $(COLLECTIONS_DIR)

.PHONY: install_colls
install_colls: colls_dir ## Install the necessary ansible collections
	@ansible-galaxy collection install -p $(COLLECTIONS_DIR) community.general
	@ansible-galaxy collection install -p $(COLLECTIONS_DIR) community.libvirt
	@ansible-galaxy collection install -p $(COLLECTIONS_DIR) containers.podman

.PHONY: all
all: venv colls_dir install_colls ## Executes all
