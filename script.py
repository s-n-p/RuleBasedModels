from libsbml import *
from echoSBML import *

## This is how you create an SBML document that uses the multi package.
def createDocument():
	ns = SBMLNamespaces (3, 1, "multi", 1)
	doc = SBMLDocument(ns)
	doc.setPackageRequired("multi", True)
	return doc

## Read arbitrary SBML files.
def readDocument(filename):
	doc = readSBML(filename)
	return doc

## Checks if document violates any SBML rule.
def validateDocument(doc):
	if doc.getNumErrors() > 0:
		if doc.getError(0).getErrorId() == XMLFileUnreadable:
			# Handle case of unreadable file here.
			doc.printErrors()
		elif doc.getError(0).getErrorId() == XMLFileOperationError:
			# Handle case of other file error here.
			doc.printErrors()
		else:
			# Handle other error cases here.
			doc.printErrors()



if __name__ == '__main__':
#    print doc.getNumErrors()
    

    filename = "MM/MM_sbml.xml"
    echo(filename, 'testfile')
    doc = readDocument(filename)
    model = doc.getModel()
    validateDocument(doc)

    level = doc.getLevel();
    version = doc.getVersion();
   
    print("\n" + "File: " + filename + " (Level " + str(level) + ", version " + str(version) + ")" );
   
    model = doc.getModel();
   
    if (model == None):
        print("No model present." );
#       return 1;
   
    idString = "  id: "
    if (level == 1):
        idString = "name: "
        id = "(empty)"
    if (model.isSetId()):
        id = model.getId()
        print("   " + idString + id );
   
    if (model.isSetSBOTerm()):
       print("      model sboTerm: " + model.getSBOTerm() );
       
       print("functionDefinitions: " + str(model.getNumFunctionDefinitions()) );
       print("    unitDefinitions: " + str(model.getNumUnitDefinitions()) );
       print("   compartmentTypes: " + str(model.getNumCompartmentTypes()) );
       print("        specieTypes: " + str(model.getNumSpeciesTypes()) );
       print("       compartments: " + str(model.getNumCompartments()) );
       print("            species: " + str(model.getNumSpecies()) );
       print("         parameters: " + str(model.getNumParameters()) );
       print(" initialAssignments: " + str(model.getNumInitialAssignments()) );
       print("              rules: " + str(model.getNumRules()) );
       print("        constraints: " + str(model.getNumConstraints()) );
       print("          reactions: " + str(model.getNumReactions()) );
       print("             events: " + str(model.getNumEvents()) );
       print("\n");
 
   
   
	## Prints out raw xml
    print(writeSBMLToString(doc))

	## Example how core elements (compartments) and package elements (multi) are
	## retrieved.
    for comp in model.getListOfCompartments():
        multiPlugin = comp.getPlugin("multi")
        if multiPlugin != None:
            for ref in multiPlugin.getListOfCompartmentReferences():
                print('Compartment: ' + comp.getId() + ' Compartment Reference: ' + ref.getCompartment())
                   		
