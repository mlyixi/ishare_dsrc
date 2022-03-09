# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: ishare.py
import sys, config, requests, requests.packages.urllib3.util.connection as urllib3_cn, socket, os
from tabulate import tabulate
import helper.request as query
from downloader.downloader import Downloader
from installer.installer import Installer

def allowed_gai_family():
    family = socket.AF_INET
    return family


urllib3_cn.allowed_gai_family = allowed_gai_family

def help():
    helpString = '\n    Usage ishare [action] [param]\n\n    action:\n        search  :   Search images\n        pull    :   Download image\n        detail  :   Detail information of image\n        help    :   Show this help page\n\n    Example\n    - ishare search vios\n    - ishare pull vios-3.4.5\n    - ishare detail vios-3.4.5\n    '
    print helpString


def pull(name):
    if not os.path.isfile('/opt/unetlab/html/store/app/pnetlab'):
        print 'Sorry, ishare not support this platform'
        return
    result = query.get(config.SERVER + '/api/user/ishare/detail?action=download&name=' + name)
    if not result['result']:
        print result['message']
    image = result['data']
    fileDownloader = Downloader()
    try:
        if fileDownloader.download(image):
            imageInstaller = Installer()
            imageInstaller.install(image, fileDownloader)
            print 'Download image successfully'
            print '===========NOTE============'
            print image['image_des']
            fileDownloader.release()
        else:
            print 'Can not download image'
            fileDownloader.release()
    except (KeyboardInterrupt, Exception) as e:
        fileDownloader.release()
        print e


def getInfo(name):
    result = query.get(config.SERVER + '/api/user/ishare/detail?name=' + name)
    if not result['result']:
        print result['message']
    data = []
    x = result['data']
    data.append([x['image_name'], x['image_type'], x['image_size'], x['image_des']])
    print ''
    print tabulate(data, headers=['Name', 'Type', 'Size', 'Description'])
    print '---------------------------------------------'
    print 'To Pull image use command: ishare pull [Name]'
    print ''


def search(search):
    result = query.get(config.SERVER + '/api/user/ishare/search?search=' + search)
    if not result['result']:
        print result['message']
    data = []
    for x in result['data']:
        data.append([x['image_name'], x['image_type'], x['image_size']])

    print ''
    print tabulate(data, headers=['Name', 'Type', 'Size'])
    print '---------------------------------------------'
    print 'To Pull image use command: ishare pull [Name]'
    print ''


def main():
    argvs = sys.argv
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        help()
        return
    action = argvs[1]
    if action == 'pull':
        name = argvs[2]
        pull(name)
    if action == 'search':
        searchData = argvs[2]
        search(searchData)
    if action == 'detail':
        name = argvs[2]
        getInfo(name)


main()
# okay decompiling ishare_extracted/ishare.pyc
