To use the program from the command line type

python main_script.py <sbml_file_path> <delta_size> <seconds>

Delta is the desired delta for Euler's ODE simulation

Seconds is the how long to run the simulation

For example, the number of steps would be seconds / delta.  Best results for MM_sbml_sbmlmulti.xml
are achieved by using delta = 0.0005 and seconds = 2