#coding = utf-8
import sys
import libtorrent
import re
class GetTorrentInfo(object):
    def __init__(self , filename = None):
        self.bt = libtorrent.bdecode(self.open_file(filename))
    
        
    @staticmethod
    def open_file(filename = None):
        if len(sys.argv) >= 2:
            with open(sys.argv[1] , 'rb') as f:
                return f.read()
        else:
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

    @staticmethod
    def hasDirectory(input_data):
        if re.match('.*path.*' , str(input_data)):
            return True
        else:
            return False

    def getFileName(self):
        info_dict = self.bt['info']
        if self.hasDirectory(info_dict):
            files_list = info_dict['files']
            result = []
            for i in files_list:
                result.append(i['path'])
            return result
        else:
            return info_dict['name']
    
        
        
def main():
    filename = 'test4.torrent'
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

if __name__ == '__main__':
    while True:
        main()
        if raw_input():
            break
    
    
