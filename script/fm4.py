#!/usr/bin/env python

#Alexander Kutschera, 2018-09-02
#The original script was written by Christop Glaubitz (https://chrigl.de/, Download: https://chrigl.de/~chris/fm4/)
#Changes are commented

import sys
import simplejson
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime

streams = [
    ('4HOPWed', 'House Of Pain'),
    ('4ULMon', 'Unlimited'),
    ('4ULTue', 'Unlimited'),
    ('4ULWed', 'Unlimited'),
    ('4ULThu', 'Unlimited'),
    ('4ULFri', 'Unlimited'),
    ('4SSUSun', 'Sunny Side Up'),
    ('4CHSat', 'Charts'),
    ('4ZSSun', 'Zimmerservice'),
    ('4JZFri', 'Jugend-Zimmer'),
    ('4DDSat', 'Davi Decks'),
    ('4ISSun', 'Im Sumpf'),
    ('4HEMon', 'Heartbeat'),
    ('4HSTue', 'High Spirits'),
    ('4TVThe', 'Tribe Vibes'),
    ('4SHFri', 'Salon Helga'),
    ('4GLSun', 'Graue Lagune'),
    ('4PHTue', 'Fivas Ponyhof'),
    ('4CZWed', 'Chez Hermez'),
    ('4BTThu', 'Bonustrack'),
    ('4PXFri', 'Project X'),
    ('4LBFri', 'La Boum de Luxe'),
    ('4SSSat', 'Swound Sound System'),
    ('4LRMon', 'Liquid Radio'),
    ('4DKMSun', 'Digital Konfusion'),
    ('4SOPMon', 'Soundpark'),
    ]

try:
    if sys.hexversion >= 50331648:
        from urllib.request import urlopen
    else:
        from urllib2 import urlopen
except ImportError:
    print("Unable to run this script. urlopen not available.")

def search_in_playlist():
    """ deprecated? No new data since beginnig of Apr 2013 """
    f = urlopen('http://onapp1.orf.at/webcam/fm4/fod/spezialmusik.xspf')
    xml_s = f.read()
    f.close()

    xml = ET.fromstring(xml_s)
    ns = {'n': 'http://xspf.org/ns/0/'}

    for track in xml.findall('./n:trackList/n:track', namespaces=ns):
        title = track.find('./n:title', namespaces=ns)
        if title is not None and 'House of Pain' in title.text:
            location = track.find('./n:location', namespaces=ns)
            if location is not None:
                return location.text
    return None

def search_in_json(stream): #changed function to look for multiple show streams
    """ from audioapi.orf.at. Have a look into http://fm4.orf.at/radio/stories/fm4houseofpain """
    # no exception handling because I want to know if it does not work
    now_s = datetime.now().strftime('%s')+'000'
    f = urlopen('http://audioapi.orf.at/fm4/json/2.0/playlist/%s?callback=&_=%s' % (stream, now_s))

    json_s = f.read()
    f.close()
    res = simplejson.loads(json_s)
    parts = res['streams'] #check num of streams in the json
    if len(parts) == 1: #regular download of single stream
        loop_stream_id = res['streams'][0]['loopStreamId']
        return 'http://loopstream01.apa.at/?channel=fm4&ua=flash&id=%s' % loop_stream_id

    else:
        urls = list() #if there are more then one parts the respective urls are returned in a list
        for stream in parts:
            loop_stream_id = stream['loopStreamId']
            urls.append('http://loopstream01.apa.at/?channel=fm4&ua=flash&id=%s' % loop_stream_id)
        return urls

def show_list():
    """ just guessed """
    for s in streams:
        print('%s - %s'% s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get fm4 stream url')
    parser.add_argument('--stream', '-s', default='4HOPWed', help='name of stream, e.g. 4HOPWed (House Of Pain) 4ULMon (Unlimited of the last monday)')
    parser.add_argument('--list', '-l', action='store_true')
    args = parser.parse_args()
    if args.list:
        show_list()
        sys.exit(0)
    res = search_in_json(args.stream)
    if res:
        print(res)
