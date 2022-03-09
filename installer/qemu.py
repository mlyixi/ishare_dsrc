# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: installer/qemu.py
import os, shutil, subprocess

def process(image, downloader):
    qemuDir = '/opt/unetlab/addons/qemu'
    target = downloader.getTarget()
    print 'Scand all files downloaded and paste to Qemu'
    for path, subdirs, files in os.walk(target):
        if len(subdirs) > 0:
            for name in subdirs:
                folderPath = os.path.join(path, name)
                folderName = os.path.basename(folderPath)
                folderName = folderName.replace(' ', '_')
                newFolder = qemuDir + '/' + folderName
                if os.path.isdir(newFolder):
                    answer = ''
                    while answer != 'y' and answer != 'n':
                        answer = raw_input('Qemu ' + folderName + " is already existed. Do you want to delete? [y/n](answer 'n' to merge folder): ")
                        if answer == 'y':
                            shutil.rmtree(newFolder)
                            shutil.move(folderPath, newFolder)
                        elif answer == 'n':
                            pass
                        else:
                            print 'Please enter y or n.'

                else:
                    shutil.move(folderPath, newFolder)

        elif len(files) > 0:
            folderName = image['image_name'].split('/')[0]
            folderName = folderName.replace(' ', '_')
            newFolder = qemuDir + '/' + folderName
            if os.path.isdir(newFolder):
                answer = ''
                while answer != 'y' and answer != 'n':
                    answer = raw_input('Qemu ' + folderName + " is already existed. Do you want to delete? [y/n](answer 'n' to merge folder): ")
                    if answer == 'y':
                        shutil.rmtree(newFolder)
                        os.makedirs(newFolder)
                    elif answer == 'n':
                        pass
                    else:
                        print 'Please enter y or n.'

            else:
                os.makedirs(newFolder)
            for name in files:
                filePath = os.path.join(path, name)
                fileName = os.path.basename(filePath)
                newFile = newFolder + '/' + fileName
                print 'Copy to ' + newFile
                if os.path.isfile(newFile):
                    answer = ''
                    while answer != 'y' and answer != 'n':
                        answer = raw_input(fileName + ' is already existed. Do you want to overwritten? [y/n]: ')
                        if answer == 'y':
                            os.remove(newFile)
                            shutil.move(filePath, newFolder)
                        elif answer == 'n':
                            pass
                        else:
                            print 'Please enter y or n.'

                else:
                    shutil.move(filePath, newFolder)

        else:
            return

    for path, subdirs, files in os.walk(newFolder):
        for name in files:
            filePath = os.path.join(path, name)
            if filePath.find('.yml') != -1:
                shutil.move(filePath, '/opt/unetlab/html/templates')

    subprocess.check_output('sudo chmod 755 -R ' + newFolder, shell=True)
# okay decompiling qemu.pyc
