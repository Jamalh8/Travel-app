#!/bin/bash
echo "updating system"
sudo apt update
echo "installing python and dependencies"
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
echo "Starting venv"
source venv/bin/activate
echo "installing requirements"
pip3 install -r requirements.txt
echo "killing any existing processes"
sudo kill $(cat gunicornpidfile)
python3 create.py
echo "running on gunicorn with pid stored in file"
python3 -m gunicorn -b -D 0.0.0.0:5000 -w 4 application:app  -p gunicornpidfile