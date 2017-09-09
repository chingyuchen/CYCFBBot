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
from pgm import Pgm

################################################################################

# The dict that maps the commands to the corresponding pgm class name.
command_class = {}

# The dict that maps the commands to the corresponding pgm class.
command_library = {}

with open('commandsmap.json', 'r') as fp:
    command_class = json.load(fp)
fp.close()

for key in command_class:
    try:
        command_library[key] = locate(command_class[key])()
    except:
        print(key + " class not exist")
    
    
################################################################################

def add_cmdpgm(pgmcmd):
    if type(pgmcmd) is str:
        pgm = Pgm(pgmcmd)
        command_library[pgmcmd] = pgm
    else:
        raise TypeError("Command of the new program must be string")

#------------------------------------------------------------------------------

def get_pgmstates(pgmcmd):
    if type(pgmcmd) is str:
        if pgmcmd in command_library:
            return command_library[pgmcmd].statefun.keys()
        else:
            raise ValueError("Program doesn't exist")
    else:   
        raise TypeError("Command of the program must be string")

#------------------------------------------------------------------------------

def remove_cmdpgm(pgmcmd):
    if type(pgmcmd) is str:
        if pgmcmd == "/start" or pgmcmd == "/default":
            raise ValueError("start or default program can't be removed. Can be overwrite instead.")
        elif pgmcmd in command_library:
            command_library.pop(pgmcmd)
            return True
        else:
            raise ValueError("Program doesn't exist")
    else:
        raise TypeError("Command of the program must be string")
        return False

#------------------------------------------------------------------------------

def add_pgm_state(pgmcmd, statename, check_cmd_function, state_function):
    if statename is None or check_cmd_function is None or state_function is None:
        raise ValueError("Input arguments can't be None")
    if pgmcmd not in command_library:
        raise ValueError("Program doesn't exist. Use add_cmdpgm to add the pgm first.")
    else:
        pgm = command_library[pgmcmd]
        pgm.add(statename, check_cmd_function, state_function)

#------------------------------------------------------------------------------

def set_pgm_state(pgmcmd, statename, check_cmd_function=None, state_function=None):
    if statename is None or (check_cmd_function is None and state_function is None):
        raise ValueError("Input arguments can't be None")
    elif pgmcmd not in command_library:
        raise ValueError("Program doesn't exist. Use add_cmdpgm add the pgm first.")
    else:
        pgm = command_library[pgmcmd]
        pgm.set(statename, check_cmd_function, state_function)

#------------------------------------------------------------------------------

def remove_pgm_state(pgmcmd, statename):
    if type(pgmcmd) is not str or type(statename) is not str:
        raise TypeError("arguments must be string")
    elif pgmcmd not in command_library:
        raise ValueError("Program doesn't exsit, Use add_cmdpgm add pgm first.")
    elif statename == "START":
        raise ValueError("START state can't be removed. Can be overwrite instead")
    else:
        pgm = command_library[pgmcmd]
        pgm.remove(statename)


