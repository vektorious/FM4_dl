#!/usr/bin/env bash

echo "Updating..." &&

sudo apt-get update &&
sudo apt-get dist-upgrade &&

git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
$chmod +x dropbox_uploader.sh
$./dropbox_uploader.sh
