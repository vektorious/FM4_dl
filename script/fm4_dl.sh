#!/usr/bin/env bash

#SHOW_URL="$(sudo python fm4.py -s '4HOPWed')" #insert you favourite show tag here
SHOW_URL="https://www.abendzeitung-muenchen.de/media.media.43b9b948-2982-473a-8401-6ae566a63557.original1024.jpg"
DATE=`date +%Y-%m-%d`

wget -O ../downloads/HOP/${DATE}_HOP.mp3 ${SHOW_URL}
