#!/usr/local/bin/python3.4
'''
Created on 28-Dec-2016

@author: kapil
'''
from tkinter.filedialog import askdirectory
from os import listdir,path,replace
from os import walk
import random
import string
import csv
import tkinter



def numberGenerator( low,high):
    return random.randint(low,high)

def createFile(filename):
    print('enter the number of  rows/data length')
    rows=int(input())
    print('enter the number of  colummn length')
    colnum=int(input())
    rangearr=[]
    col=0
    print(colnum)
    while(col!=int(colnum)):
        print('enter the '+str(col)+' column\'s lower and upper limit')
        rangearr.append(input())
        rangearr.append(input())
        col=col+1
        print(col)
    with open(filename, mode='a') as fp:
        writer=csv.writer(fp,delimiter='!')
        for i in range(0,rows):
            for j in range(0,colnum):
                #writer.write(numberGenerator(2*j,2*j+1))
                fp.write(str(numberGenerator(int(rangearr[2*j]),int(rangearr[2*j+1])))+' ')
                
            fp.write('\n')
root=tkinter.Tk()
root.withdraw()
foldername=askdirectory(parent=root,title='please select directory for creating file')
print(foldername)
print(' enter the filename to be produced')
filename=input()
createFile(path.join(foldername,filename))
        