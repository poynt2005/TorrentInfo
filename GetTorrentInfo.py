#coding = utf-8
import sys
import libtorrent
from getFile import Torrent2Magnet as T2M
import re

class GetTorrentInfo(object):
    def __init__(self , filename = None):
        
        #check if sys.argv is defined
        if len(sys.argv) >= 2:
            filename = sys.argv[1]
        
        #check if filename is a magnet link
        if re.match('^magnet\:\?xt\=urn\:btih\:.*' , filename):
            self.getTorrentFile(filename)
        else :
            self.bt = libtorrent.bdecode(self.open_file(filename))
    
        
    @staticmethod
    def open_file(filename = None):         
        if not filename == None:
            with open(filename , 'rb') as f:
                return f.read()
    
    def get_magnet(self):
        info = libtorrent.torrent_info(self.bt)
        name = ''
        if ' ' in info.name():
            name = info.name().replace(' ', '_')
        else:
            name = info.name()
        return 'magnet:?xt=urn:btih:%s&dn=%s' % (info.info_hash(),name)

    #check if the torrent has directories
    @staticmethod
    def hasDirectory(input_data):
        if re.match('.*path.*' , str(input_data)):
            return True
        else:
            return False

    def getFileName(self):
        #it's a dictionary data , get files' name
        info_dict = self.bt['info']
        if self.hasDirectory(info_dict):
            files_list = info_dict['files']
            result = []
            for i in files_list:
                result.append(i['path'])
            return result
        else:
            return info_dict['name']
        
    @staticmethod
    def getTorrentFile(magnet_link):
        torrent_file = T2M(magnet_link)
        torrent_file.getTorrent()
        
        
def main():

    filename = None
    link = None
    
    if len(sys.argv) >= 2:
        string = sys.argv[1]
        if re.match('^magnet\:\?xt\=urn\:btih\:.*' , string):
            link = string
        else:
            filename = string

    if filename:
        a = GetTorrentInfo(filename)
        print 'Magnet Link is : \n%s' % (a.get_magnet())
        print 
        res = a.getFileName()
        if isinstance(res , list):
            print 'This file may have directory :'
            for i in res:
                print 'File name is : %s' % (i)
            print 
        else:
            print 'File name is : %s' % (res)
    if link:
        b = GetTorrentInfo(link)

if __name__ == '__main__':
    main()
