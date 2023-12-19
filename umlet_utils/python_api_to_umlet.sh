#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
. $SCRIPT_DIR/../venv/bin/activate
python $SCRIPT_DIR/python_api_to_umlet.py "$@"
