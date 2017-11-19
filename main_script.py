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



def printList(listname):
    for i in listname:
        print i






def main (filename):
    print 'ECHO: '
    echo(filename, 'testfile')
    print '\nread_sbml: '
    print read_sbml.read_sbml(filename)
    print '\nprintMath: '
    printMath.main(filename)
    reader = SBMLReader()
    doc = reader.readSBMLFromFile(filename)
    model = doc.getModel() 
    
    species = [model.getSpecies(i) for i in range(model.getNumSpecies())]
    printList(species)
    
    params = model.getListOfParameters()
    printList(params)
    
    reactions = model.getListOfReactions()
    printList(reactions)
    for r in reactions:
        print r, formulaToString(r.getKineticLaw().getMath())






if __name__ == '__main__':   
    filename = "MM/MM_sbml.xml"
    main(filename)  






