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
        wx.Frame.__init__(self, None, -1, "The Text Analyser", size=(300, 300))
        
        filemenu = wx.Menu()
        helpmenu = wx.Menu()
        ################################
       # menuNew  = filemenu.Append(wx.ID_NEW, "N&ew game")
        menuOld  = filemenu.Append(wx.ID_OPEN,"O&pen File")
       #menuSave = filemenu.Append(wx.ID_SAVE,"S&ave current game")
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
        #self.Bind(wx.EVT_MENU, self.ExitProgram, menuExit)
        #self.Bind(wx.EVT_MENU, self.OnAbout,  menuAbout)
        #self.Bind(wx.EVT_MENU, self.LoadFile, menuOld)
        #self.Bind(wx.EVT_MENU, self.displaygame, self.currentgamebutton)
        #self.Bind(wx.EVT_MENU, self.Save, menuSave)

        self.SetMenuBar(menuBar)
        self.CreateStatusBar() # A StatusBar in the bottom of the window
        panel = wx.Panel(self, -1)
    

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

list =  string.split()

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

