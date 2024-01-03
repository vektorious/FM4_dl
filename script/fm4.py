#!/usr/bin/env python

#Alexander Kutschera, 2018-09-02
#The original script was written by Christoph Glaubitz (https://chrigl.de/, Download: https://chrigl.de/~chris/fm4/)
#Changes are commented

import sys
import simplejson
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime
import time

streams = [
    ('4CH', 'Charts'),
    ('4CZ', 'Chez Hermez'),
    ('4DD', 'Davi Decks'),
    ('4DKM', 'Digital Konfusion'),
    ('4DLL', 'Dalia\'s Late Night Lemonade'),
    ('4FP', 'Film Podcast'),
    ('4GL', 'Graue Lagune'),
    ('4GP', 'Worldwide Show'),
    ('4GPC', 'Game Podcast'),
    ('4HE', 'Heartbeat'),
    ('4HF', 'Hallo FM4'),
    ('4HH', 'Happy Hour'),
    ('4HS', 'High Spirits'),
    ('4HOP', 'House Of Pain'),
    ('4IS', 'Im Sumpf'),
    ('4LB', 'La Boum de Luxe'),
    ('4LL', 'Lieblingslieder'),
    ('4LR', 'Liquid Radio'),
    ('4MGMon', 'Morgengrauen (Monday)'),
    ('4MGTue', 'Morgengrauen (Tuesday)'),
    ('4MGWed', 'Morgengrauen (Wednesday)'),
    ('4MGThu', 'Morgengrauen (Thursday)'),
    ('4MGFri', 'Morgengrauen (Friday)'),
    ('4MOMon', 'Morning Show (Monday)'),
    ('4MOTue', 'Morning Show (Tuesday)'),
    ('4MOWed', 'Morning Show (Wednesday)'),
    ('4MOThu', 'Morning Show (Thursday)'),
    ('4MOFri', 'Morning Show (Friday)'),
    ('4MOSat', 'Morning Show (Saturday)'),
    ('4MOSun', 'Morning Show (Sunday)'),
    ('4MPC', 'Musik Podcast'),
    ('4OKMon', 'OKFM4 (Monday)'),
    ('4OKTue', 'OKFM4 (Tuesday)'),
    ('4OKWed', 'OKFM4 (Wednesday)'),
    ('4OKThu', 'OKFM4 (Thursday)'),
    ('4OKFri', 'OKFM4 (Friday)'),
    ('4PH', 'Fivas Ponyhof'),
    ('4PSMon', 'Passt Show (Monday)'),
    ('4PSTue', 'Passt Show (Tuesday)'),
    ('4PSWed', 'Passt Show (Wednesday)'),
    ('4PSThu', 'Passt Show (Thursday)'),
    ('4PSFri', 'Passt Show (Friday)'),
    ('4PX', 'Project X'),
    ('4SPSun', 'Soundpark'),
    ('4SS', 'Swound Sound'),
    ('4SSUSun', 'Sunny Side Up'),
    ('4TV', 'Tribe Vibes'),
    ('4UL', 'Unlimited'),
    ('4ZS', 'Zimmerservice'),
    ]

try:
    if sys.hexversion >= 50331648:
        from urllib.request import urlopen
    else:
        from urllib2 import urlopen
except ImportError:
    print("Unable to run this script. urlopen not available.")

def search_in_json(stream): # changed function to look for multiple show streams
    """ from audioapi.orf.at. Have a look into https://fm4.orf.at/radio/stories/fm4houseofpain """
    # no exception handling because I want to know if it does not work
    #now_s = datetime.now().strftime('%s')+'000' does not work on windows
    now_s = str(int(time.time()))+'000'
    f = urlopen('https://audioapi.orf.at/fm4/json/2.0/playlist/%s?callback=&_=%s' % (stream, now_s))
    json_s = f.read()
    f.close()
    res = simplejson.loads(json_s)
    # JSON structure changed (e.g. https://audioapi.orf.at/fm4/json/2.0/playlist/4LB). The "last" broadcast 
    # day of the show contains always the current stream 
    parts = res[len(res)-1]['streams'] #check num of streams in the json
    if len(parts) == 1: #regular download of single stream
        loop_stream_id = res[len(res)-1]['streams'][0]['loopStreamId']
        return 'https://loopstream01.apa.at/?channel=fm4&ua=flash&id=%s' % loop_stream_id

    else:
        urls = list() #if there are more then one parts the respective urls are returned in a list
        for stream in parts:
            loop_stream_id = stream['loopStreamId']
            urls.append('https://loopstream01.apa.at/?channel=fm4&ua=flash&id=%s' % loop_stream_id)
        return urls

def show_list():
    """ just guessed """
    for s in streams:
        print('%s - %s'% s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get fm4 stream url')
    parser.add_argument('--stream', '-s', default='4HOP', help='name of stream, e.g. 4HOP (House Of Pain) 4UL (Unlimited of the last Friday)')
    parser.add_argument('--list', '-l', action='store_true')
    args = parser.parse_args()
    if args.list:
        show_list()
        sys.exit(0)
    res = search_in_json(args.stream)
    if res:
        print(res)
