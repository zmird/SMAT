# Variables
COLLECTIONS_DIR := ./collections

# Targets
# ------------------------------------------------------------------------------

# Create the collections directory if it doesn't exist
.PHONY: create_dir
create_dir:
	mkdir -p $(COLLECTIONS_DIR)

# Install the containers.podman collection to the collections directory
# This target depends on the create_dir target to ensure the directory
# is created before provisioning the virtual machine
.PHONY: install
install: create_dir
	ansible-galaxy collection install -p $(COLLECTIONS_DIR) containers.podman
	ansible-galaxy collection install -p $(COLLECTIONS_DIR) community.libvirt

# Creates virtual env
.PHONY: venv
venv: 
	python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
