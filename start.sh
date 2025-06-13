#!/bin/bash

echo "Installing Chrome..."
apt-get update && apt-get install -y wget unzip curl
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb || apt --fix-broken install -y

echo "Installing ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
wget -N https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

echo "Running script..."
python3 main.py