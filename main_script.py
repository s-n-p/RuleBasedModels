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
    reader = SBMLReader()
    doc = reader.readSBMLFromFile(filename)
    model = doc.getModel() 
    
#    print 'ECHO: '
#    echo(filename, 'testfile')
    print '\nGet validation errors: \n'
    errors = doc.getNumErrors()
    if errors == 0:
        print 'No Errors'
    else:
        print read_sbml.read_sbml(filename)
    print '\n PRINT MATH: \n'
    printMath.main(filename)

    
    species = [model.getSpecies(i) for i in range(model.getNumSpecies())]
    print '\n SPECIES: \n'
    printList(species)
    print str(species[0]).split()
    
    params = model.getListOfParameters()
#    p = model.getParameter(0)
#    print p
    print '\n PARAMETERS: \n'
    printList(params)
    for i in params:
        print i.getValue()
    
    reactions = model.getListOfReactions()
    print '\n REACTIONS: \n'
    for r in reactions:
        print r, formulaToString(r.getKineticLaw().getMath())
        
    assignments = model.getListOfInitialAssignments()
    print '\n ASSIGNMENTS: \n'
    for a in assignments:
        print str(a), formulaToString(a.getMath())
        
#    comp = model.getListOfCompartments()
#    print comp
#    for c in comp:
#        print c





if __name__ == '__main__':   
    filename = "MM/MM_sbml.xml"
    main(filename)  






