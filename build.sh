#!/bin/bash
echo "Installing packages"
sudo apt install python3 python3-pip python3-venv -y
echo "Setting up venv"
python3 -m venv venv
source venv/bin/activate
echo "Installing dependencies"
pip3 install -r requirements.txt
echo "Running unit tests"
python3 -m pytest tests/test_app.py --cov=application --cov-report=html
echo "copying files from jenkins to app-server"
scp -r application jenkins@app-server:/home/jenkins/
scp app.py jenkins@app-server:/home/jenkins
scp create.py jenkins@app-server:/home/jenkins
scp requirements.txt jenkins@app-server:/home/jenkins
echo "Deploying app"
ssh jenkins@app-server < deploy.sh