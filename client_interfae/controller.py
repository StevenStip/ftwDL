__author__ = 'steven'
import requests
import json
import urllib
import os
import datetime
import iso8601
from django.db import IntegrityError
from models import Fling, Sender, Media


class Api:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.timestampFilename = 'last_update'
        self.lastRecordedTime = self.loadTimestamp()

    def getNewItems(self):
        """
        GET https://api.superfling.com/api/v2/flings HTTP/1.1
        Authorization: Bearer b7b41e94e516854c894d20700d50dd61bc09d62167a954b8c298f06d03659f04
        If-Modified-Since: 2015-10-06 19:58:03 +0000
        Host: api.superfling.com
        Connection: Keep-Alive
        Accept-Encoding: gzip
        User-Agent: okhttp/2.2.0
        """
        modifiedsince = str(self.lastRecordedTime)
        print "get new Items"
        url = 'https://api.superfling.com/api/v2/flings'
        # Needs updating
        headers = {"Authorization": "Bearer b7b41e94e516854c894d20700d50dd61bc09d62167a954b8c298f06d03659f03",
                   "If-Modified-Since": modifiedsince, 'Host': 'api.superfling.com',
                   'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/2.2.0'}
        r = requests.get(url=url, headers=headers)
        print r.status_code
        print r
        if r.status_code == 200:
            response_document = r.json()
            # print response_document
            print response_document
            for fling in response_document['flings']:

                filestring = "{0}-{1}".format(fling['created_at'], fling['country'])
                filename = ""
                if fling['media']['type'] == 'Image':
                    filename = 'images/' + filestring + '.jpg'
                    self.download(fling['media']['url'], filename)

                if fling['media']['type'] == 'Video':
                    filename = 'videos/' + filestring + '.mp4'
                    self.download(fling['media']['url'], filename)
                sp = fling['payload']['sender']
                if not (sp == None or filename == ""):
                    print fling
                    media_text = ""
                    if fling['media']['text'] != None:
                        media_text = fling['media']['text']
                    m, created = Media.objects.get_or_create(type=fling['media']['type'], url=fling['media']['url'],
                                                             local_path=filename, text=media_text)
                    print "id:{}, jid:{}, first_name:{}".format(sp['id'], sp['jid'], sp['first_name'])
                    s, created = Sender.objects.get_or_create(id=sp['id'], jid=sp['jid'], first_name=sp['first_name'])
                    f = Fling(id=fling['id'], created_at=fling['created_at'], country=fling['country'],
                              media=m,
                              sender=s)

                    # s.save()
                    # m.save()
                    f.save()

                try:
                    print fling['country'] + " - " + fling['payload']['sender']['first_name']
                    print fling['media']['url'] + " " + fling['media']['text']

                except KeyError as e:
                    print "missing parameter " + e.message
                except TypeError as e:
                    print e.message

                self.upTimestamp(fling['created_at'])
                # print "fling in flinglist: "
                # print fling
            res = "there were {0} new flings since {1} and the most recent one is from {2}".format(
                    len(response_document['flings']), modifiedsince, self.lastRecordedTime)
            print res
            return res
        return "no new ones"

    def download(self, url, filename):
        urllib.urlretrieve(url, os.path.join(self.dir_path, "static/" + filename))

    def upTimestamp(self, timestamp):
        if iso8601.parse_date(timestamp) > self.lastRecordedTime:
            self.lastRecordedTime = iso8601.parse_date(timestamp)
            f = open(os.path.join(self.dir_path, self.timestampFilename), 'w+')
            f.write(timestamp)
            f.close()

    def loadTimestamp(self):
        with open(os.path.join(self.dir_path, self.timestampFilename)) as f:
            return iso8601.parse_date(f.read())


if __name__ == "__main__":
    c = Api()
    # c.download("https://s3-eu-west-1.amazonaws.com/unii-fling/original_c2bbcb978dd9e6688f7a1d4259f8f0fd.jpg",'images/test.jpg')
    # c.getNewItems(modifiedSince='2015-10-15 05:58:03 +0000')

    c.getNewItems()
