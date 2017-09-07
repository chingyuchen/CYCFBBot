################################################################################
''' 
File: cmdlibrary.py
Author : Ching-Yu Chen

Description: cmdlibrary.py contains a dict that maps the commands to all the 
program classes of a designed facebook bot. The list of corresponding commands 
and the name of the classes are in the commandsmap.json. 

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

from pydoc import locate
import json

################################################################################

# The dict that maps the commands to the corresponding pgm class name.
command_class = {}

# The dict that maps the commands to the corresponding pgm class.
command_libarary = {}

with open('commandsmap.json', 'r') as fp:
    command_class = json.load(fp)
fp.close()

for key in command_class:
    try:
        command_libarary[key] = locate(command_class[key])()
    except:
        print(key + " class not exist")
    
    
################################################################################

def add_cmdpgm(pgmcmd):
    pgm = Pgm(pgmcmd)
    cmd_libarary[pgmcmd] = pgm

def remove_cmdpgm(pgmcmd):
    if pgmcmd in cmd_library:
        cmd_library.pop()
        return True
    else:
        return False

def add_pgm_state(pgmcmd, statename, check_cmd_function, state_function):
    if pgmcmd not in cmd_library:
        print("error, no such program exist")
        return
    # check other arguments valid
    # check if statename exist already
    pgm = cmd_library[pgmcmd]
    pgm.add(statename, check_cmd_function, state_function)

def set_pgm_state(pgmcmd, statename, check_cmd_function=None, state_function=None):
    #check arguments
    pgm = cmd_library[pgmcmd]
    pgm.set(statename, check_cmd_function, state_function)

def remove_pgm_state(pgmcmd, statename):
    # check valid/can remove 
    pgm = cmd_library[pgmcmd]
    pgm.remove(statename)

   
