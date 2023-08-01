#!/usr/bin/env bash

export GIT_REPO_PATH=$(git rev-parse --show-toplevel)

export HOST_IP=192.168.122.1

export MAAS_EXTERNAL_IP=192.168.122.2
export MAAS_SSH_KEY="$GIT_REPO_PATH/roles/role_smat/files/maas-key"
