
# SpyWatcher - Discord File Scanner
SpyWatcher source is a bot for discord that scans files sent by users in your server, It will
Download and scan the files through (VirusTotal) with over 73 Anti-Virus Engines, Aswell
as including Md5 Scanning and Hash Scanning.

# File Scanning
**For File Scans and Uploads It will scan each message for attatchments and if detected will download the
attatched file to a cache folder, Next it will get the Md5 Hash of the downloaded file and scan it using the VirusTotal Engine API.
Next will it return the information needed through a JSON format which will be returned to the user.**

![alt text](https://github.com/Zurek0x/SpyWatcher/blob/main/media/sc1.png?raw=true)

# MD5 Scanning ($md5 HASH)
**MD5 Scanning works the same as File Scanning in terms of the file scanning but skips the download and upload part,
If the user knows the Md5 Hash of the file they are trying to scan they can use command ( $md5 HASH ) replacing HASH with the MD5
Hash you are trying to scan, Which will go through the same process as the File Scan and return the information needed in a JSON Format which will
be returned to the user.**

![alt text](https://github.com/Zurek0x/SpyWatcher/blob/main/media/sc2.png?raw=true)

# Console Logs
**Console Logs don't really matter all to much but give a LOG for all files detected, scanned, uploaded and more.**
![alt text](https://github.com/Zurek0x/SpyWatcher/blob/main/media/sc3.png?raw=true)


# Setup
**install required libraries**
```bash
pip install -r requirements.txt
```
**Edit bot.cfg with your token & api key for virus total**
```config
[inf]
token=TOKEN
virusTotal_APIkey=API
```
* **To get a API Key for Virus Total go to the website https://www.virustotal.com/ And create a account and login, Next under your profile options you will see a option for API Key or Your API Key, There you shall find your personal API Key, This will give you access to Malware Scanning and so on.**

# Notes | bot.py
```python
46) exceptions=['png', 'jpg', 'jpeg', 'gif'] # Put in File Extension without the .
47) # Files to Except or Not Scan.
```

# Change-Log
> Version 1.4.1
> * **Fixed P.u.t call to VirusTotal Engine**
> * **Switched from Private to Public on Github page**
>
> Version 1.3
> * **Updated Menu Class for discord.ui.View (FIX)**
> * **Added Exception List to file uploads**
>
> Version 1.2
> * **Added Manual MD5 Hash Scanning ($md5 HASH)**
>
> Version 1.1
> * **Added Form Style Buttons to Embed Message**
>
> Version 1.0
> * **Added File Detection and Downloading of Files**
> * **Added VirusTotal API for Engine Scanning**
>
