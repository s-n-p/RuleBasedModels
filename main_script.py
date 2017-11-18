# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:13:32 2017

@author: spenc
"""

from libsbml import *
from echoSBML import *
import sys
import os.path
import libsbml
import read_sbml
import printMath










def main (filename):
    print 'ECHO: '
    echo(filename, 'testfile')
    print '\nread_sbml: '
    print read_sbml.read_sbml(filename)
    print '\nprintMath: '
    printMath.main(filename)
#    libsbml.
    reader = SBMLReader()
    doc = reader.readSBMLFromFile(filename)
    model = doc.getModel()   
    species = [model.getSpecies(i) for i in range(model.getNumSpecies())]
    for i in species:
        print i






if __name__ == '__main__':   
    filename = "MM/MM_sbml.xml"
    main(filename)  






