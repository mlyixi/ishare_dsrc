# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: installer/docker.py
import os, shutil, subprocess

def process(image, downloader):
    target = downloader.getTarget()
    print 'Scand all files downloaded and load to docker'
    for path, subdirs, files in os.walk(target):
        for name in files:
            filePath = os.path.join(path, name)
            subprocess.call('docker load < ' + filePath, shell=True)
# okay decompiling docker.pyc
