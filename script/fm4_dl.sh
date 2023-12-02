#!/usr/bin/env bash
cd "$(dirname "$0")" #set wd to file location
SHOW_TAGS=(4UL 4DKM 4DD 4LB)  #insert you favourite show tags here
STORAGE=/music
i=1
for SHOW_TAG in "${SHOW_TAGS[@]}"; do
  echo $SHOW_TAG
  URL="$(python fm4.py -s ${SHOW_TAG}| tr -d '[],')" #call python script to get the stream URL
  mkdir -p ${STORAGE}/${SHOW_TAG} #creates show directory if it doesn't exist
  echo $URL
  URL="${URL%\'}" #removes the starting quote
  URL="${URL#\'}" #removes the last quote
  DATE="${URL#*id=}"
  echo $DATE
  DATE="${DATE%%_*}"
  wget -O ${STORAGE}/${SHOW_TAG}/${DATE}_${SHOW_TAG}_${i}.mp3 ${URL} #download show
  #../Dropbox-Uploader/dropbox_uploader.sh upload ../downloads/${SHOW_TAG}/${DATE}_${SHOW_TAG}_${i}.mp3 /${SHOW_TAG}/2018-08-23_${SHOW_TAG}.mp3
  #upload to Dropbox folder: remove the line above if you don't want to use the dropbox uploader
  let "i=i+1"
done
