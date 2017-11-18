# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:35:33 2017

@author: spenc
"""

import sys
import os.path
import libsbml
 
def echo (infile, outfile):
  """usage: echoSBML.py input-filename output-filename
  """
#   if len(args) != 3:
#     print(main.__doc__)
#     sys.exit(1)
 
#   infile  = args[1]
#   outfile = args[2]
  if not os.path.exists(infile):
    print("[Error] %s : No such file." % (infile))
    sys.exit(1)
 
  reader  = libsbml.SBMLReader()
  writer  = libsbml.SBMLWriter()
  sbmldoc = reader.readSBML(infile)
 
  if sbmldoc.getNumErrors() > 0:
    if sbmldoc.getError(0).getErrorId() == libsbml.XMLFileUnreadable:
       # Handle case of unreadable file here.
      sbmldoc.printErrors()
    elif sbmldoc.getError(0).getErrorId() == libsbml.XMLFileOperationError:
       # Handle case of other file error here.
      sbmldoc.printErrors()
    else:
       # Handle other error cases here.
      sbmldoc.printErrors()
 
    sys.exit(1)
     
  writer.writeSBML(sbmldoc, outfile)
  print("[OK] Echoed %s to %s" % (infile, outfile))
 
# if __name__ == '__main__':
#   main(sys.argv)  