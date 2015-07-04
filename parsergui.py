#!/usr/bin/python

import wx
import os
import os.path

#debug = 1
debug = 0

#by christopher rehm
#may 25 2015
"""a simple program that does word count in a txt document """
"""will possibly upgrade it to something that does more later """
if debug == 1:
    print("hello world")
    print("file to open")

""" the basic architecture is simple. a data object is created at start up """
""" then the data object creates a display and allows the user to select a file to be checked"""
""" then the display object updates the display. if the user desires she can save the analysis"""
""" which is saved in a text file, in lines so that it can be used as data for other programs"""

#############################################################
#############################################################
#############################################################

"""the display object, a window from wxpython. contains all code relating to display of data"""

class MyFrame(wx.Frame):
    def __init__(self, Datablock):
        wx.Frame.__init__(self, None, -1, "The Text Analyser", size=(600, 470))
        self.panel = wx.Panel(self, -1) 
        #make frame aware of where to find data for display
        self.dataadr = Datablock
        filemenu = wx.Menu()
        helpmenu = wx.Menu()
        ################################
        menuOld  = filemenu.Append(wx.ID_OPEN,"O&pen File")
        menuSave = filemenu.Append(wx.ID_SAVE,"S&ave current analysis")
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
        self.Bind(wx.EVT_MENU, self.Save, menuSave)

        self.SetMenuBar(menuBar)
        self.CreateStatusBar() # A StatusBar in the bottom of the window
        self.displayTitles(self.panel)
        self.updateDataDisplay("","","" , self.panel)
      

    ################################################################################

    def ExitProgram(self, event):
        self.Close(True)
        self.Destroy()

    #######################################################################################
    
    def OnAbout(self, event):
        pass

    ######################################################################################
    
    def LoadFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename =dlg.GetFilename()
            self.dirname  =dlg.GetDirectory()
            filehandle=os.path.join(self.dirname, self.filename)

            #not sure if this is doing what i think it is... or why
            mydatais.analysedfile =filehandle
            if debug == 1:
                print(filehandle)
                print(mydatais.analysedfile)
            mydatais.analysefile(filehandle)
            self.displayTitles(self.panel)

#"""load up temp data holders with data from the data object then display them"""
#"""not sure why i had to do this this way but i think its an advantage, as the data in the"""
#"""data object is untouched , protects data integrity"""

            data0 = mydatais.analysedfile
            data1 = mydatais.rawwordcount
            data2 = mydatais.uniquewordcount
            #self.updateDataDisplay("      ","          ","               ", self.panel)
            self.updateDataDisplay(data0, data1, data2, self.panel)

    #####################################################################################
           
    def Save(self, event):
        pass

    #########################################################################

    def displayTitles(self, panel):
        txt1 =wx.StaticText(panel, -1, "name of file analysed",              pos=(20,20 ))
        txt2 =wx.StaticText(panel, -1, "total number of words in file",      pos=(20,60 ))
        txt9 =wx.StaticText(panel, -1, "unique words in file",               pos=(20,100))
        txt3 =wx.StaticText(panel, -1, "avg number of letters per word",     pos=(20,140))
        txt4 =wx.StaticText(panel, -1, "average sentence length",            pos=(20,180))
        txt5 =wx.StaticText(panel, -1, "average clauses per sentence",       pos=(20,220))
        txt6 =wx.StaticText(panel, -1, "currently unused",                   pos=(320,260))
        txt7 =wx.StaticText(panel, -1, "currently unused",                   pos=(320,300))
        txt8 =wx.StaticText(panel, -1, "currently unused",                   pos=(320,340))

    ########################################################################

    def updateDataDisplay(self, mydataloc, data1, data2,  panel):
        txt11 =wx.StaticText(panel, -1, mydataloc,                 pos=(320,20 ))
        txt12 =wx.StaticText(panel, -1, str(data1),                pos=(320,60 ))
        txt19 =wx.StaticText(panel, -1, str(data2),                pos=(320,100))
        txt13 =wx.StaticText(panel, -1, "currently unused",        pos=(320,140))
        txt14 =wx.StaticText(panel, -1, "currently unused",        pos=(320,180))
        txt15 =wx.StaticText(panel, -1, "currently unused",        pos=(320,220))
        txt16 =wx.StaticText(panel, -1, "currently unused",        pos=(320,260))
        txt17 =wx.StaticText(panel, -1, "currently unused",        pos=(320,300))
        txt18 =wx.StaticText(panel, -1, "currently unused",        pos=(320,340))
 
    #####################################################################################  


#######################################################################################
#######################################################################################

"""the data object, that is the data from the file. it calls the display window above."""
"""data analysis is done here in this object, NOT in the display window."""


class FileDataAnalysis(object):
    def __init__(self):
        self.analysedfile ="none currently"
        self.rawwordcount = 0
        self.uniquewordcount = 0
        self.lettersperword = 0
        self.wordspersentence = 0
        self.clausespersentence = 0
        self.clausesintext = 0
        self.wordsperparagraph = 0
        self.numberofparagraphs = 0
        self.datafromfile = ""
        self.datafromfileunique = ""

        aframe = MyFrame(self)
        aframe.Show(True)
        

    ################################################################################

    def analysefile(self, filehandle):
        myfile =open(filehandle, "rb")
        newstring = myfile.read()

        """now pull out all the punctuation, and sort the words."""

        newstring = str.replace(str(newstring),"."," ")
        newstring = str.replace(str(newstring),","," ")
        newstring = str.replace(str(newstring),":"," ")
        newstring = str.replace(str(newstring),";"," ")
        newstring = str.replace(str(newstring),"\""," ")
        newstring = str.replace(str(newstring),","," ")
        newstring = str.lower(newstring)

        list =  str.split(newstring)

        if debug == 1:
            print(list)

        list2 = sorted(list)
        length = len(list2)

        if debug == 1:
            print(list2) 

        self.rawwordcount  = len(list2)

        if debug == 1:
            print("The length of your text in words is ", len(list2))

        a = 1
        ulength = length #start with unique # of words = to current file length, then delete as needed)
        while (a < ulength-1):

            if debug == 1:
                print(list2[a],list2[a+1]) #debug tool
                print("\n") #debug tool

            if list2[a] == list2[a+1]:
                list2.remove(list2[a+1])
                ulength = ulength - 1
            else:
                a = a+1
        self.uniquewordcount=ulength

        if debug == 1:
            print("The number of unique words in your text is ", self.uniquewordcount)

###############################################################
##############################################################        




#######################################################################################
#######################################################################################
#######################################################################################

if __name__ == '__main__':
    app = wx.App()
    mydatais = FileDataAnalysis()
    app.MainLoop()
