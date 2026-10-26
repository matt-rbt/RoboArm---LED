#!/usr/bin/env bash
set -eu

VENV_DIR=".venv"
PYTHON_BIN="${VENV_DIR}/bin/python"
PIP_BIN="${VENV_DIR}/bin/pip"

if [ ! -x "${PYTHON_BIN}" ]; then
    python3 -m venv "${VENV_DIR}"
fi

"${PYTHON_BIN}" -m pip install --upgrade pip
"${PYTHON_BIN}" -m pip install -r requirements.txt

mpwled() {
    "${PYTHON_BIN}" -m mpremote connect port:rfc2217://localhost:4000 "$@"
}

echo "Dependencies installed."
echo "Start Wokwi, then run the firmware with:"
echo "  ${PYTHON_BIN} -m mpremote connect port:rfc2217://localhost:4000 run firmware/main.py"
echo "or run the host script with:"
echo "  ${PYTHON_BIN} host/host.py"