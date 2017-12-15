# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 21:57:40 2017

@author: spenc
"""

import sys
import time
import os
import os.path
from libsbml import *
 
def read_sbml (filename):
   """Usage: readSBML filename
   """
   
   current = time.clock();
   document = readSBML(filename);  
   errors = document.getNumErrors();
   
   print;
   print("            filename: " + filename);
   print("           file size: " + str(os.stat(filename).st_size));
   print("      read time (ms): " + str(time.clock() - current));
   print(" validation error(s): " + str(errors));
   print;
   
   document.printErrors();
   
   return errors;
#     
#if __name__ == '__main__':
#   main(sys.argv)  