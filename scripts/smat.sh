#!/bin/bash

# Function to display usage
function print_help {
    echo "Usage: $0 [-h] [-l list-targets] [-a all] [-u uninstall] [-s setup-host] [-m install-maas] [-c configure-maas] [-n install-nodes] [-j install-juju]"
    echo " "
    echo "Options:"
    echo "-h, --help                Show help"
    echo "-l, --list-targets        List all targets"
    echo "-a, --all                 Execute all install and configure targets"
    echo "-u, --uninstall           Execute the uninstall target"
    echo "-s, --setup-host          Execute the setup-host target"
    echo "-m, --install-maas        Execute the install-maas target"
    echo "-c, --configure-maas      Execute the configure-maas target"
    echo "-n, --install-nodes       Execute the install-nodes target"
    echo "-j, --install-juju        Execute the install-juju target"
    echo "    --uninstall-maas      Execute the uninstall-maas target"
    echo "    --uninstall-nodes     Execute the uninstall-nodes target"
    echo "    --uninstall-juju      Execute the uninstall-juju target"
}

# Variable to store arguments
TARGET=

# Check if no arguments were passed and print help
if [ $# -eq 0 ]; then
  print_help
  exit 0
fi

# Parse command-line arguments
while (( "$#" )); do
  case "$1" in
    -h|--help)
      print_help
      exit 0
      ;;
    -l|--list-targets)
      TARGET="list-targets"
      shift
      ;;
    -s|--setup-host)
      TARGET="setup-host"
      shift
      ;;
    -m|--install-maas)
      TARGET="install-maas"
      shift
      ;;
    -c|--configure-maas)
      TARGET="configure-maas"
      shift
      ;;
    -n|--install-nodes)
      TARGET="install-nodes"
      shift
      ;;
    -j|--install-juju)
      TARGET="install-juju"
      shift
      ;;
    --uninstall-maas)
      TARGET="uninstall-maas"
      shift
      ;;
    --uninstall-nodes)
      TARGET="uninstall-maas"
      shift
      ;;
    -u|--uninstall)
      TARGET="uninstall"
      shift
      ;;
    -a|--all)
      TARGET="all"
      shift
      ;;
    --) # End of all options
      shift
      break
      ;;
    -*|--*=) # Unsupported flags
      echo "Error: Unsupported flag $1" >&2
      exit 1
      ;;
    *) # Preserve positional arguments
      print_help 
      exit 0
      ;;
  esac
done

ROOT_DIR=$(git rev-parse --show-toplevel)

if [[ $TARGET == "list-targets" ]]; then
  echo "install"
  echo "setup-host"
  echo "install-maas"
  echo "configure-maas"
  echo "install-nodes"
  echo "install-juju"
  echo "uninstall"
  echo "uninstall-maas"
  echo "uninstall-nodes"
elif [[ $TARGET == "all" ]]; then
  echo "Executing all targets."
  echo "Sudo password is needed, please enter it below."
  cd $ROOT_DIR && \
    source scripts/env.sh && \
    ansible-playbook -K playbooks/juju.yml -i inventories/maas.py --tags install
elif [[ $TARGET == "install-juju" ]]; then
  cd $ROOT_DIR && \
    source scripts/env.sh && \
    ansible-playbook -K playbooks/juju.yml -i inventories/maas.py --tags $TARGET
else
  echo "Executing target $TARGET."
  echo "If sudo password is needed, please enter it below."
  cd $ROOT_DIR && \
    source scripts/env.sh && \
    ansible-playbook -K playbooks/smat.yml -i inventories/maas.py --tags $TARGET
fi
