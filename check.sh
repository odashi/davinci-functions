#!/bin/bash

# Usage:
#   On the root directory of the repository:
#   $ python3 -m venv venv
#   $ source venv/bin/activate
#   $ python -m pip install '.[dev]'
#   $ ./check.sh

GREEN='\033[1;32m'
RED='\033[1;31m'
NC='\033[0m'
CLEAR='\033[2K\r'

run() {
    echo -n RUNNING: $@
    LOG_FILE=$(mktemp)
    $@ >${LOG_FILE} 2>${LOG_FILE}
    if [ $? -eq 0 ]; then
        echo -e ${CLEAR}${GREEN}PASSED: $@${NC}
    else
        echo -e ${CLEAR}${RED}FAILED: $@${NC}
        echo
        cat ${LOG_FILE}
        echo
    fi
    rm ${LOG_FILE}
}

run python -m pytest src -vv
run python -m black --check src
run python -m pflake8 src
run python -m isort --check src
run python -m mypy src
