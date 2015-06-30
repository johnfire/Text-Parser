#!/usr/bin/python

import wx
import os
import os.path


#by christopher rehm
#may 25 2015
#a simple program that does word count in a txt document
#will possibly upgrade it to something that does more later

print("hello world")
print("file to open")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "The Text Analyser", size=(600, 470))
        
        panel = wx.Panel(self, -1)
        filemenu = wx.Menu()
        helpmenu = wx.Menu()
        ################################
       # menuNew  = filemenu.Append(wx.ID_NEW, "N&ew game")
        menuOld  = filemenu.Append(wx.ID_OPEN,"O&pen File")
        menuSave = filemenu.Append(wx.ID_SAVE,"S&ave current game")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"Q&uit")
        ################################
        menuHelp = helpmenu.Append(wx.ID_HELP,"H&elp")
        menuSet  = helpmenu.Append(6,"Settings")
        helpmenu.AppendSeparator()
        menuAbout = helpmenu.Append(wx.ID_ABOUT,"A&bout")
        ################################
        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(helpmenu,"&Help")
        menuBar.SetBackgroundColour('White')
        ###################################
        self.Bind(wx.EVT_MENU, self.ExitProgram, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout,  menuAbout)
        self.Bind(wx.EVT_MENU, self.LoadFile, menuOld)
        #self.Bind(wx.EVT_MENU, self.displaygame, self.currentgamebutton)
        self.Bind(wx.EVT_MENU, self.Save, menuSave)

        self.SetMenuBar(menuBar)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        self.filename = "none"
        self.numberofwords = 0
        self.avgwordcount = 0
        self.avgsentencelength = 0
        self.avgnumberofwordspara = 0

        ######################################
        #static text on the panel
        #####################################
        txt1 =wx.StaticText(self,-1,"Name of file being analysed", pos=(20,20))
        txt2 =wx.StaticText(self,-1,"Number of words in file", pos=(20,60))
        txt9 =wx.StaticText(self,-1,"Number of unique words in file", pos=(20,100))
        txt3 =wx.StaticText(self,-1,"Average word length",pos=(20,140))
        txt4 =wx.StaticText(self,-1,"Average sentence length",pos=(20,180))
        txt5 =wx.StaticText(self,-1,"Average number of words per paragraph",pos=(20,220))
        txt6 =wx.StaticText(self,-1,"Number of paragraphs",pos=(20,260))
        txt7 =wx.StaticText(self,-1,"Reserved for future use",pos=(20,300))
        txt8 =wx.StaticText(self,-1,"Reserved for future use",pos=(20,340))

         
       

    def ExitProgram(self, event):
        self.Destroy()
    
    def OnAbout(self, event):
        pass
    
    def LoadFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            self.control=[]
            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'rb')
            newstring = filehandle.read()
            newstring = str.replace(str(newstring),"."," ")
            newstring = str.replace(str(newstring),","," ")
            newstring = str.replace(str(newstring),":"," ")
            newstring = str.replace(str(newstring),";"," ")
            newstring = str.replace(str(newstring),"\""," ")
            newstring = str.replace(str(newstring),","," ")
           # newtring = str.lower()

            list =  str.split(newstring)
            list2 = sorted(list)
            length = len(list2)
            #print list2  #debug tool

            self.numberofwords = len(list2)
            #print "The length of your text in words is ", len(list2)
            a = 1
            while (a < length-1):
                #print list2[a],list2[a+1] #debug tool
                #print "\n" #debug tool
                if list2[a] == list2[a+1]:
                    list2.remove(list2[a+1])
                    length = length - 1
                else:
                    a = a+1
            self.numberofdifwords=len(list2)
#p#rint "The number of unique words in your text is ",  len(list2)
#print list2
            #output
            txt11 =wx.StaticText(self,-1,self.filename, pos=(320,20))
            txt12 =wx.StaticText(self,-1,str(self.numberofwords), pos=(320,60))
            txt19 =wx.StaticText(self,-1,str(self.numberofdifwords),pos=(320,100))
            txt13 =wx.StaticText(self,-1,str(self.avgwordcount), pos=(320,140))
            txt14 =wx.StaticText(self,-1,str(self.avgsentencelength), pos=(320,180))
            txt15 =wx.StaticText(self,-1,str(self.avgnumberofwordspara),pos=(420,220))
            txt16 =wx.StaticText(self,-1,"0",pos=(320,260))
            txt17 =wx.StaticText(self,-1,"0",pos=(320,300))
            txt18 =wx.StaticText(self,-1,"0",pos=(320,340))

    def Save(self, event):
        pass


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()

#txtfile = raw_input()
#txt=open(txtfile, "r")
#print "your file to be broken down is ",txtfile

#string = txt.read()
#string = string.replace("."," ")
#string = string.replace(","," ")
#string = string.replace(":"," ")
#string = string.replace(";"," ")
#string = string.replace("\""," ")
#string = string.replace(","," ")
#string = string.lower()

#list =  string.split()

#print list #debug tool
#print "\n" #debug tool

#list2 = sorted(list)
#print list2  #debug tool

#length = len(list2)
#print "The length of your text in words is ", len(list2)
#a = 1
#while (a < length-1):
   #print list2[a],list2[a+1] #debug tool
   #print "\n" #debug tool
   #if list2[a] == list2[a+1]:
   #   list2.remove(list2[a+1])
   #   length = length - 1
   #else:
   #   a = a+1
 
#p#rint "The number of unique words in your text is ",  len(list2)
#print list2

