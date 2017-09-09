################################################################################
'''
File: pgmabstract.py
Author : Ching-Yu Chen

Description: pgmabstract.py contains the abstract class, PgmAbstract, where 
PgmAbstract is the abstract class of the command program in facebook bot.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

from pymessenger.bot import Bot

################################################################################

class Pgm(object):

    '''
    PgmAbstract is an abstract class of the command program in facebook bot. 
    Subclass must define the functions to execute / check valid command function
    / enum of the state in each state of the program. 

    '''

#--------------------------- state function example ----------------------------

    def check_start(self, data=None):

        '''
        Function to check valid command at start state. Return true if it is 
        valid, otherwise return false.
        '''    
        
        return True


    def state_start(self, user, msg=None, args = None):

        '''
        Start state function. After check_start function check the command is 
        valid, the state function then can be execute. Return the next state
        and args.
        '''    

        self.bot.send_text_message(user, "This is {pgmcmd} program start "\
                "state".format(pgmcmd=self.pgmcmd))

        return ["END", None]


#---------------------------- Initialization -----------------------------------

    def __init__(self, pgmcmd):

        '''
        Initialized the command program object. The subclasses must define 
        self.statefun and self.check_cmd.
        '''

        # pgmcmd
        self.pgmcmd = pgmcmd
        
        # Token of the bot.
        TOKEN = ""
        with open('Token', 'r') as f:
            TOKEN = f.read().strip()
        f.close()

        
        # Object of pymessenger.bot, sending and receiving messages to facebook users
        self.bot = Bot(TOKEN)
        
        # self.statefun, the list stores the state function.
        self.statefun = {"START": self.state_start} 
        
        # self.check_cmd, the list stores the check command function.
        self.check_cmd = {"START": self.check_start} 


#--------------------------- Inherit method ------------------------------------
    
    def run(self, user, state, msg_content=None, args=None):

        ''' 
        Execute the pgm in specified state, user, msg and args. Return the next
        state of the program.
        '''

        try:
            next_stateinfo = self.statefun[state](user, msg_content, args)
            assert(next_stateinfo != None)
            return next_stateinfo
        except:
            raise NotImplementedError('State function must return next state inform')


#------------------------------------------------------------------------------

    def add(self, statename, check_cmd_function, state_function):
        # check function 
        if statename is None or check_cmd_function is None or state_function is None:
            raise ValueError("Input arguments can't be None")
        if type(statename) is not str:
            raise TypeError("statename must be string")
        else:
            self.statefun[statename] = state_function
            self.check_cmd[statename] = check_cmd_function
    
#------------------------------------------------------------------------------

    def set(self, statename, check_cmd_function=None, state_function=None):
        # check function 
        if statename is None or (check_cmd_function is None and state_function is None):
            raise ValueError("Input arguments can't be None")
        if check_cmd_function is not None:
            self.check_cmd[statename] = check_cmd_function
        if state_function is not None:
            self.statefun[statename] = state_function

#------------------------------------------------------------------------------

    def remove(self, statename):
        if statename not in self.statefun:
            raise ValueError("State doesn't exist.")
        elif statename == "START":
            raise ValueError("START state can't be removed")
        else:
            self.statefun.pop(statename)
            self.check_cmd.pop(statename)
