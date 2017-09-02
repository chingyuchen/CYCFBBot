################################################################################
'''
File: pgmabstract.py
Author : Ching-Yu Chen

Description: pgmabstract.py contains the abstract class, PgmAbstract, where 
PgmAbstract is the abstract class of the command program in facebook bot.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import abc
from abc import ABCMeta
from pymessenger.bot import Bot

################################################################################

class PgmAbstract(object, metaclass=ABCMeta):

    '''
    PgmAbstract is an abstract class of the command program in facebook bot. 
    Subclass must define the functions to execute / check valid command function
    / enum of the state in each state of the program. 

    '''

    __metaclass__ = abc.ABCMeta
    
#---------------------------- Initialization -----------------------------------

    def __init__(self):

        '''
        Initialized the command program object. The subclasses must define 
        self.statefun and self.check_cmd.
        '''
        
        # Token of the bot.
        TOKEN = ""
        with open('Token', 'r') as f:
            TOKEN = f.read().strip()
        f.close()

        
        # Object of pymessenger.bot, sending and receiving messages to facebook users
        self.bot = Bot(TOKEN)
        
        # self.statefun, the list stores the state function.
        try:
            len(self.statefun) != 0
        except:
            raise NotImplementedError('Subclasses must define statefun')

        
        # self.check_cmd, the list stores the check command function.
        try:
            len(self.check_cmd) != 0
        except:
            raise NotImplementedError('Subclasses must define check_cmd')


#--------------------------- Inherit fields ------------------------------------

    '''
    Enum of the state, specified the index of the state function/check function 
    in the list objects self.statefun and self.check_cmd.
    '''
    
    @property
    def START():
        return 0

    
    @property
    def END():
        return -1

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


#--------------------------- Abstract field ------------------------------------

    @property
    @abc.abstractmethod
    def name():

        '''
        The corresponding command of the program
        '''
        
        pass

#--------------------------- Abstract method -----------------------------------

    @abc.abstractmethod
    def check_start(self, data=None):

        '''
        Function to check valid command at start state. Return true if it is 
        valid, otherwise return false.
        '''    

        pass


    @abc.abstractmethod
    def state_start(self, user, msg=None, args = None):

        '''
        Start state function. After check_start function check the command is 
        valid, the state function then can be execute. Return the next state
        and args.
        '''    

        pass

    

