# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:13:32 2017

@author: spenc
"""
from __future__ import division
from libsbml import *
import echoSBML
import sys
import os.path
import libsbml
import printMath
import read_sbml
import matplotlib.pyplot as plt
import sys

   
def validate(document):
    print '\nVALIDATION: \n'
    errors = document.getNumErrors()
    document.printErrors()
    if errors == 0:
        print 'No Errors'
        return 0
    else:
        print 'Validation errors found: \n'
        document.printErrors()
        return 1

def params_dict(p, assignments):
    parameters = {}
    for i in p:
        parameters[i.getId()] = float(i.getValue())
    for a in assignments:
        parameters[a.getId()] = float(compute(formulaToString(a.getMath()), parameters))
    return parameters

def species_cons(listOfSpecies):
    species_list = {}
    species_cons = {}
    for sp in listOfSpecies:
        species_list[sp.getId()] = sp.getName()
        species_cons[sp.getId()] = [sp.getInitialConcentration()]
#            multiPlugin = sp.getPlugin("multi")
#            if multiPlugin != None:
#                for con in multiPlugin.initialConcentration():
#                    print con
    return species_list, species_cons

def compute(formula, params):
    for k, v in enumerate(params):
        if v in formula:
            formula = formula.replace(v, str(params[v]))
    return eval(formula)

def get_dSpecies(species, reactants, products, formulas):
    diff_equs = {}
    for i in species:
        diff_equs[i] = ''
        for r in reactants:
            if i in reactants[r]:
                diff_equs[i] += '-( '+formulas[r]+' )'
            if i in products[r]:
                diff_equs[i] += ' + ' + formulas[r]
    return diff_equs
        
def get_reactants_products(reactions):
    reactants = {}
    products = {}
    formulas = {}
    for r in reactions:
        species = r.getName()
#        i = r.getId()
        formulas[species] = formulaToString(r.getKineticLaw().getMath())
        reactants[species] = []
        products[species] = []
#        print 'reaction: ', r.getName()
        rs = r.getListOfReactants()
        pd = r.getListOfProducts()
        for rt in rs:
            reactants[species].append(rt.getSpecies()) 
        for pdt in pd:
            products[species].append(pdt.getSpecies())
    return reactants, products, formulas

def put_params_in_DE(diff_eqs, params):
    for i in diff_eqs:
        eq = diff_eqs[i]
#        print i, ' : ', eq
        for p in params:
            if p in eq:
                eq = eq.replace(str(p), str(params[p]))

            diff_eqs[i] = eq
    return diff_eqs
    
def evaluate(diff_eqs, cons, delta, steps):
    for step in xrange(steps):
        new_diff_eqs = {}
        for i in diff_eqs:
            if bool(diff_eqs[i]):
                eq = diff_eqs[i]
                for c in cons:
                    if c in eq:
                        eq = eq.replace(c, str(cons[c][-1]))              
            else:
                eq = '0.0'
            new_diff_eqs[i] = eq           
        cons = get_new_cons(new_diff_eqs, cons)
    return cons
    
def get_new_cons(diff_eqs, cons):
    cons_change = {}
    for i in diff_eqs:
        cons_change[i] = float(eval(diff_eqs[i]))
    for i in cons:
        cons[i].append(cons[i][-1] + cons_change[i])
    return cons

def show_plot(running_cons, species, steps, delta):
    legend = []
    for s in species:
        plt.plot(range(steps+1), running_cons[s])
        legend.append(species[s])
    plt.legend(legend, loc='upper center', fontsize = 'xx-large')
    plt.title(filename, fontsize='xx-large')
    plt.show()
    

def main (filename, delta, seconds):  
    steps = int(seconds / delta)
    reader = SBMLReader()
    doc = reader.readSBMLFromFile(filename)
    valid = validate(doc)
    if valid == 0:
        model = doc.getModel()
    
        print '\nPRINT MATH:\n'
        printMath.main(filename)
       
        species, cons = species_cons(model.getListOfSpecies())
        print '\nSPECIES ID\'S: \n'
        print species, '\n'
        print '\nINITIAL CONCENTRATIONS: \n'
        print cons
        
        print '\nPARAMETERS: \n'
        params = params_dict(model.getListOfParameters(), model.getListOfInitialAssignments())
        print params
        
        print '\nREACTIONS: \n'
        reactants, products, formulas = get_reactants_products(model.getListOfReactions())
#        print formulas
        diff_eqs = get_dSpecies(species, reactants, products, formulas)
        diff_eqs = put_params_in_DE(diff_eqs, params)
        
        running_cons = evaluate(diff_eqs, cons, delta, steps)
        
        show_plot(running_cons, species, steps, delta)



       
            
    #    comp = model.getListOfCompartments()
    #    print comp
    #    for c in comp:
    #        print c
    
    	## Example how core elements (compartments) and package elements (multi) are
    	## retrieved.
#        for comp in model.getListOfCompartments():
#            multiPlugin = comp.getPlugin("multi")
#            print multiPlugin.getListOfCompartmentReferences()
#            if multiPlugin != None:
#                for ref in multiPlugin.getListOfCompartmentReferences():
#                    print('Compartment: ' + comp.getId() + ' Compartment Reference: ' + ref.getCompartment())
#            else:
#                print 'NONE'
#                    
#        for sp in model.getListOfSpecies():
#            multiPlugin = sp.getPlugin("multi")
#            if multiPlugin != None:
#                for ref in multiPlugin.getListOfOutwardBindingSites():
#                    print ref.getComponent()
#    #                print('Compartment: ' + comp.getId() + ' Compartment Reference: ' + ref.getCompartment())
#        

                
        
#        print species_list, '\n', species_cons
            
#            multiPlugin = sp.getPlugin("multi")
#            if multiPlugin != None:
#                for ref in multiPlugin.getListOf:
#                    print ref.getComponent()

if __name__ == '__main__':   
    argArray = sys.argv
    filename = argArray[1]
    delta = float(argArray[2])
    seconds = float(argArray[3])
    main(filename, delta, seconds)  
