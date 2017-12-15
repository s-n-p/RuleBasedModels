# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 11:56:24 2017

@author: spenc
"""

import sys
import time
import os
import os.path
from libsbml import *
 
 #
 #Translates the given infix formula into MathML.
 #
 #@return the MathML as a string.  The caller owns the memory and is
 #responsible for freeing it.
 #
def translateInfix(formula):
    math = parseFormula(formula);
    return writeMathMLToString(math);
 
 # 
 # Translates the given MathML into an infix formula.  The MathML must
 # contain no leading whitespace, but an XML header is optional.
 # 
 # @return the infix formula as a string.  The caller owns the memory and
 # is responsible for freeing it.
 # 
def translateMathML(xml):
    math = readMathMLFromString(xml);
    return formulaToString(math);
 
def main (args):    
    print 'ENTERED MAIN'
    print("This program translates infix formulas into MathML and");
    print("vice-versa.  Enter or return on an empty line triggers");
    print("translation. Ctrl-C quits");
    sb = ""  
    try:
        while True:
            print("Enter infix formula or MathML expression (Ctrl-C to quit):");
            print "> ",
           
            line = sys.stdin.readline()
            while line != None:
                trimmed = line.strip();
                length = len(trimmed);
                if (length > 0):
                    sb = sb + trimmed;
                else:
                    str = sb;
                    result = ""
                    if (str[0] == '<'):
                        result = translateMathML(str)
                    else:
                        result =  translateInfix(str)
    
                    print("Result:\n\n" + result + "\n\n");
                    sb = "";
                    break;
     
                line = sys.stdin.readline()
    except:
        return 0;
    return 0;
 
if __name__ == '__main__':
    print 'ENTERED MAIN'
    main(sys.argv)  