# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: installer/dynamips.py
import os, shutil

def process(image, downloader):
    dynamipDir = '/opt/unetlab/addons/dynamips'
    target = downloader.getTarget()
    print 'Scand all files downloaded and paste to Dynamips'
    for path, subdirs, files in os.walk(target):
        for name in files:
            filePath = os.path.join(path, name)
            fileName = os.path.basename(filePath)
            newFile = dynamipDir + '/' + fileName
            print 'Copy to ' + newFile
            if os.path.isfile(newFile):
                answer = ''
                while answer != 'y' and answer != 'n':
                    answer = raw_input('Dynamips ' + fileName + ' is already existed. Do you want to overwritten? [y/n]: ')
                    if answer == 'y':
                        os.remove(newFile)
                        shutil.move(filePath, dynamipDir)
                        os.chmod(newFile, 493)
                    elif answer == 'n':
                        pass
                    else:
                        print 'Please enter y or n.'

            else:
                shutil.move(filePath, dynamipDir)
                os.chmod(newFile, 493)
# okay decompiling dynamips.pyc
