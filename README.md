# FM4 - Stream Downloader

### Summary
This repository contains everything what you need to (automatically) download the .mp3 files of your favorite streams from the Austrian [radio station FM4](https://fm4.orf.at/)! (+ optional upload to your Dropbox)

### Why?

The Austrian [radio station FM4](https://fm4.orf.at/) has great "genre shows" (like ["House of Pain"](https://fm4.orf.at/radio/stories/fm4houseofpain/)) in the evening but unfortunately they are only available for seven days and only via [web player](https://fm4.orf.at/player/) or smartphone app. Sometimes I forget to listen to the latest show or I am at places where I have no access to internet and I urgently want to listen to my favorite radio show.

That's why I was looking into a way to download the mp3s of the shows to solve all my problems. There were already some people out there who developed programs for downloading the streams. I used the python script from [Chris](https://chrigl.de/~chris/fm4/) to retrieve the stream mp3 url from the [FM4 API](http://audioapi.orf.at/fm4/json/2.0/broadcasts/) and added some lines to also enable a complete download if the show consists out of multiple mp3 files ([here is my fm4.py version](https://raw.githubusercontent.com/vektorious/FM4_dl/master/script/fm4.py)).

I added a bash script to automatically download the mp3s of a specific stream and upload it to my Dropbox. I set up a cron job on my Pi so I won't miss any show anymore 🎉

### Instructions

Clone this repository:

```bash
git clone https://github.com/vektorious/FM4_dl
cd FM4_dl/scripts
```
#### Retrieve MP3 URLs

Now you can already get the stream mp3 urls:

```bash
python fm4.py -s **insert show tag**
```
The tags can be found in ```script\fm4.py```

For example:

```bash
python fm4.py -s "4HOP"

>>> ['http://loopstream01.apa.at/?channel=fm4&ua=flash&id=2018-08-29_2100_tl_54_4HOPWed1_63490.mp3', 'http://loopstream01.apa.at/?channel=fm4&ua=flash&id=2018-08-29_2200_tl_54_4HOPWed2_63492.mp3']

```
#### Install rclone (optional)

If you want to upload your files to a cloud service, use rclone. It supports Dropbox, Google Drive, Hetzner Storage Box, SFTP, SMB / CIFS or the local filesystem (and much many more, see https://rclone.org/) 

#### Automatically download MP3s

Make the fm4_dl.sh script executable and adjust it to your needs:

```bash
cd scripts
sudo nano fm4_dl.sh
```

Insert your favorite show tags (variable SHOW_TAGS) and storage location (STORAGE) in the script. You can find out your shows tag by looking at the [FM4 API](http://audioapi.orf.at/fm4/json/2.0/broadcasts/) or in the list in the fm4.py file

Then just run it!

```bash
bash fm4_dl.sh
```

#### Setting up a cron job on a Raspberry Pi

I let the script run as a cron job (weekly)

Open
```bash
sudo nano /etc/crontab -e
```

and insert:
```bash
25 21   * * 4   pi      /home/pi/scripts/FM4_dl/script/fm4_dl.sh
```

It is important that you let the script run as the same user as when you installed the Dropbox-Uploader because otherwise the uploader won't work!

### That's it!

Thank you for visiting this repository! If you should find any bugs or have problems getting the script to run don't hesitate to [contact me](https://twitter.com/alexwastooshort)!
