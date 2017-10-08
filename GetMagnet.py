import GetTorrentInfo
import sys
from Tkinter import *
from tkFileDialog import askopenfilename
import os

class torrentGUI(object):

    
    
    def __init__(self):
        

        
            
        
        self.win = Tk()
        self.win.title('Get Torrent Info')
        self.win.resizable(12,12)
        Label(self.win ,  bg='red', text = 'File path :').grid()
        
        path_var = StringVar()
        self.magnet_label = None
        
        
        Label(self.win , textvariable = path_var).grid()

        
        if len(sys.argv) >= 2:
            filepath = sys.argv[1]
            path_var.set(filepath)
            self.processing(filepath)
             
        
        self.btn = Button(self.win , text = 'Choose File' , command = lambda : self.callback(path_var)).grid(row = 2)
        
        
        
        Frame(self.win , width = 200 , height = 50).grid()
        
    def callback(self , var):
        filepath = askopenfilename()
        var.set(filepath)
        self.processing(filepath)
        

       
    
    def processing(self , pathname):

        getTorrent = GetTorrentInfo.GetTorrentInfo(pathname)
        magnet_url = getTorrent.get_magnet()

    
        
        magnet_var = StringVar()
        magnet_var.set(magnet_url)

        if self.magnet_label:
            self.magnet_label.grid_forget()


        self.magnet_label = Entry(self.win , width = 50 , textvariable = magnet_var)        
        self.magnet_label.grid(row = 4)


try:
    a = torrentGUI()

    a.win.mainloop()
except Exception, errormsg:
    print "Script errored!"
    print "Error message: %s" % errormsg
    print "Traceback:"
    import traceback
    traceback.print_exc()
    print "Press return to exit.."
    raw_input()

