# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: installer/installer.py
import iol, docker, qemu, dynamips

class Installer:

    def __init__(self):
        pass

    def install(self, image, downloader):
        imageType = image['image_type']
        if imageType == 'iol':
            iol.process(image, downloader)
        if imageType == 'dynamips':
            dynamips.process(image, downloader)
        if imageType == 'qemu':
            qemu.process(image, downloader)
        if imageType == 'docker':
            docker.process(image, downloader)
# okay decompiling installer.pyc
