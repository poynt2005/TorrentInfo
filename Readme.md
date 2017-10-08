# GetTorrentInfo

## GetTorrentInfo.py
> ### print torrent files and torrent magnet
>> Usage : Open File in command line (file and .py file must in same directory)
```
python GetTorrentInfo.py test.torrent
```
>> * method *"get_magnet()"* get magnet link and returns magnet link
>> * method *"hasDirectory()"* check if the torrent has directories returns boolean
>> * method *"getFileName()"* get files name in the torrent file and returns lists contain filename

## GetMagnet.py
> ### print torrent magnet in the GUI
>> Usage : Open File in command line <u>*Experimental function*</u>
```
python GetMagnet.py test.torrent
```
>> Usage : Open files in the program
```
Click "Choose file" and open file
```

## getFile.py
> ### Convert magnet link to torrent file
> ### Save torrent file to the directory where the script is
>> Usage : open link in command line
```
python getFile.py *your magnet link*
```
>> * start libtorrent session in constructor , it'll check if the link is a vaild megnet link
>> * method *"getTorrent()"* fetch torrent metadata and convert to binary data , and than write to file

