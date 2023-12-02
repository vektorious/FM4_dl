#!/usr/bin/env bash
cd "$(dirname "$0")" #set wd to file location
SHOW_TAGS=(4UL 4DKM 4DD 4LB 4SS)  #insert you favourite show tags here
STORAGE=/mnt/storage/Musik/FM4/downloads
for SHOW_TAG in "${SHOW_TAGS[@]}"; do
  URL="$(python fm4.py -s ${SHOW_TAG}| tr -d '[],')" #call python script to get the stream URL
  mkdir -p ${STORAGE}/${SHOW_TAG} #creates show directory if it doesn't exist
  URL="${URL%\'}" #removes the starting quote
  URL="${URL#\'}" #removes the last quote
  DATE="${URL#*id=}"
  DATE="${DATE%%_*}"
  FILENAME="${STORAGE}/${SHOW_TAG}/${DATE}_${SHOW_TAG}.mp3"
  if [ ! -f ${FILENAME} ]
  then
  wget -O ${FILENAME} ${URL} #download show
  # upload to cloud ? use rclone! 
  else
  echo "skipping file ${FILENAME}, it does already exist"
  fi
done
