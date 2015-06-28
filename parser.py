#!/usr/bin/python

import wx
import os
import os.path
#by christopher rehm
#may 25 2015
#a simple program that does word count in a txt document
#will possibly upgrade it to something that does more later

print "hello world"
print "file to open"

txtfile = raw_input()
txt=open(txtfile, "r")
print "your file to be broken down is ",txtfile

string = txt.read()
string = string.replace("."," ")
string = string.replace(","," ")
string = string.replace(":"," ")
string = string.replace(";"," ")
string = string.replace("\""," ")
#string = string.replace(","," ")
string = string.lower()

list =  string.split()

#print list #debug tool
#print "\n" #debug tool

list2 = sorted(list)
#print list2  #debug tool

length = len(list2)
print "The length of your text in words is ", len(list2)
a = 1
while (a < length-1):
   #print list2[a],list2[a+1] #debug tool
   #print "\n" #debug tool
   if list2[a] == list2[a+1]:
      list2.remove(list2[a+1])
      length = length - 1
   else:
      a = a+1
 
print "The number of unique words in your text is ",  len(list2)
print list2

