"""
MIT License

Copyright (c) 2023 --卡拉马里毒药..

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import os
import random
import os.path
import configparser
from virus_total_apis import PublicApi as VirusTotalPublicApi
import hashlib

config = configparser.ConfigParser()
config.read('bot.cfg')
key=config['inf']['virusTotal_APIkey']

class Engine:
    def md5Scan(md5):
        vt = VirusTotalPublicApi(key)
        response = vt.get_file_report(md5)
        jsonData=response
        try:
            md5=jsonData['results']['md5']
            total=jsonData['results']['total']
            detected=jsonData['results']['positives']
            fileType=''
            fileSize=f'{len(md5)}'
            scanDate=jsonData['results']['scan_date']
            scanUrl=jsonData['results']['permalink']
            s=[md5, total, detected, fileType, fileSize, scanDate, scanUrl, 'MD5 Scanned', 'MD5 Scanned']
        except:
            s=['No Info', 'No Info', 'No Info', 'No Info', 'No Info', 'No Info', 'No Info', 'MD5 Scanned', 'MD5 Scanned']
        return s
    def scanFile(cachedir, filename, filetype):
        load=os.stat(f'{cachedir}//{filename}')
        md5=hashlib.md5(open(f'{cachedir}//{filename}','rb').read()).hexdigest()
        vt = VirusTotalPublicApi(key)
        response = vt.get_file_report(md5)
        jsonData=response
        try:
            md5=jsonData['results']['md5']
            total=jsonData['results']['total']
            detected=jsonData['results']['positives']
            fileType=filetype
            fileSize=str(round(load.st_size / (1024 * 1024), 2))
            scanDate=jsonData['results']['scan_date']
            scanUrl=jsonData['results']['permalink']
            s=[md5, total, detected, fileType, fileSize, scanDate, scanUrl, cachedir, filename]
        except:
            s=['No Info', 'No Info', 'No Info', 'No Info', 'No Info', 'No Info', 'No Info', cachedir, filename]
        return s
    def inputFile(filename, filetype, url):
        clist=[]
        vid=str(random.randint(1, 192648)) # ID Of Sent files (To Avoid Cross Scanning of Same Files)
        cachedir=str(f'cache//{filename}.{vid}') # Cache ID + Name to avoid cross scanning of same files
        # Create Cache #
        os.mkdir(f'{cachedir}')
        # Download File #
        r=requests.get(url, allow_redirects=True)
        open(f'{cachedir}//{filename}', 'wb').write(r.content)
        clist.append(filename)
        # Scan File #
        getscan=Engine.scanFile(cachedir, filename, filetype)
        # Delete Cache #
        return getscan