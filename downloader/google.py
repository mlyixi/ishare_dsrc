# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: downloader/google.py
import re, sys, requests, requests.packages.urllib3.util.connection as urllib3_cn, socket, zipfile, os

def download(link, target, size=0):
    session = requests.Session()
    downloadLinkQuery = session.get(link)
    downloadLinkQuery = downloadLinkQuery.text
    downloadLink = re.search('\\"(https:\\/\\/[^\\"]+export\\\\u003ddownload)\\"', downloadLinkQuery)
    if downloadLink:
        downloadLink = downloadLink.group(1)
        downloadLink = downloadLink.replace('\\u003d', '=')
        downloadLink = downloadLink.replace('\\u0026', '&')
    else:
        print 'Can not get download link'
        return False
    matchFileName = re.search('<meta\\s*itemprop=\\"name\\"\\s*content=\\"([^\\"]+)\\">', downloadLinkQuery)
    if matchFileName:
        filename = matchFileName.group(1)
    else:
        print 'Can not get file name'
        return False
    verifyQuery = session.get(downloadLink, allow_redirects=False)
    verifyQuery = verifyQuery.text
    matchDownload = re.search('.*uc-download-link[^\\/]*(\\/[^\\"]+).*', verifyQuery)
    if matchDownload:
        link = 'https://drive.google.com' + matchDownload.group(1)
        link = link.replace('&amp;', '&')
        matchFileName = re.search('.*<span class=\\"uc-name-size\\"><a[^>]*>([^<]*)</a>\\s*\\(([^\\)]*)\\)', verifyQuery)
        if matchFileName:
            size = matchFileName.group(2)
    else:
        link = downloadLink
    path = target + '/' + filename
    print 'Download: ' + str(filename)
    print 'File size: ' + str(size)
    downloaded = 0
    with open(path, 'wb') as (f):
        response = session.get(link, stream=True)
        dl = 0
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            downloaded = round(dl / 1024 / 1024, 2)
            f.write(data)
            sys.stdout.write('Download progress: %d MB \r' % downloaded)
            sys.stdout.flush()

    print 'Download progress: %d MB \r' % downloaded
    if os.path.getsize(path) < 1000000:
        with open(path) as (f):
            if '<html>' in f.read():
                print 'Sorry, the file cannot be downloaded. Maybe too many users are downloading, or the link is faulty. Try again later. '
                return False
    if path.endswith('.zip'):
        print 'Unzip file ' + filename
        with zipfile.ZipFile(path, 'r') as (zip_ref):
            zip_ref.extractall(target)
        os.remove(path)
    return True
# okay decompiling google.pyc
