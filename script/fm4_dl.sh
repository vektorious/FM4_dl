#!/usr/bin/env bash
cd "$(dirname "$0")"
SHOW_TAG='4HOPWed' #insert you favourite show tag here
SHOW_URL="$(python fm4.py -s ${SHOW_TAG}| tr -d '[],')"
#SHOW_URL="https://www.abendzeitung-muenchen.de/media.media.43b9b948-2982-473a-8401-6ae566a63557.original1024.jpg" #just for testing
DATE=`date +%Y-%m-%d`

i=1
for URL in $SHOW_URL; do
  URL="${URL%\'}" #removes the starting quote
  URL="${URL#\'}" #removes the last quote 
  sudo wget -O ../downloads/${SHOW_TAG}/${DATE}_${SHOW_TAG}_${i}.mp3 ${URL}
  ../Dropbox-Uploader/dropbox_uploader.sh upload ../downloads/${SHOW_TAG}/${DATE}_${SHOW_TAG}_${i}.mp3 /${SHOW_TAG}/2018-08-23_${SHOW_TAG}.mp3
  let "i=i+1"
done

#
