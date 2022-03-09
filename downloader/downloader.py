# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: downloader/downloader.py
import google, uuid, os, shutil

class Downloader:

    def __init__(self):
        self.target = '/tmp/ishare/' + str(uuid.uuid4())
        if not os.path.exists(self.target):
            os.makedirs(self.target)

    def getTarget(self):
        return self.target

    def download(self, image):
        target = '/tmp/ishare'
        if image['image_link_type'] == 'google':
            result = google.download(image['image_link'], self.target, str(image['image_size']) + 'M')
            if not result:
                self.release()
            return result

    def release(self):
        if os.path.isdir(self.target):
            shutil.rmtree(self.target)
# okay decompiling downloader.pyc
