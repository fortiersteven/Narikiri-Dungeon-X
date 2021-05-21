# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:14:08 2021

@author: Steven
"""
import sys
from HelperFunctions import *



    
if __name__ == "__main__":
    
    #Parameters
    fileName = sys.argv[1]
    n = int(sys.argv[2])
    startPoint = sys.argv[3]
    step= int(sys.argv[4])
    nbObject = int(sys.argv[5])
    
    helper = HelperFunctions()
    helper.PointerHeader = sys.argv[6]
    

    #Create the script
    helper.createScript(fileName+"_script.txt", n, startPoint, step, nbObject)
    
    #Run the script
    helper.runscript(fileName)
    
    #Clean the dump file
    helper.cleanDump(fileName+"_dump.txt")
