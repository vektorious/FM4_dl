#!/usr/bin/env bash

SHOW_TAG = '4HOPWed' #insert you favourite show tag here
#SHOW_URL="$(sudo python fm4.py -s ${SHOW_TAG})"
SHOW_URL="https://www.abendzeitung-muenchen.de/media.media.43b9b948-2982-473a-8401-6ae566a63557.original1024.jpg"
DATE=`date +%Y-%m-%d`

wget -O ../downloads/${SHOW_TAG}/${DATE}_${SHOW_TAG}.mp3 ${SHOW_URL}

../Dropbox-Uploader/dropbox_uploader.sh upload ../downloads/${SHOW_TAG}/${DATE}_${SHOW_TAG}.mp3 /${SHOW_TAG}/2018-08-23_${SHOW_TAG}.mp3
