#!/usr/bin/env bash

#make this script executable (sudo chmod u+x)
echo "Updating..." &&

sudo apt-get update &&
sudo apt-get dist-upgrade &&

echo "Installing Dropbox Uploader" &&
echo "SOURCE: https://github.com/andreafabrizi/Dropbox-Uploader" &&

git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
cd Dropbox-Uploader
sudo chmod +x dropbox_uploader.sh
./dropbox_uploader.sh
