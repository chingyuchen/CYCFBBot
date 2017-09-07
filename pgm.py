################################################################################
'''
File: pgmabstract.py
Author : Ching-Yu Chen

Description: pgmabstract.py contains the abstract class, PgmAbstract, where 
PgmAbstract is the abstract class of the command program in facebook bot.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

#import abc
#from abc import ABCMeta
from pymessenger.bot import Bot

################################################################################

#class PgmAbstract(object, metaclass=ABCMeta):
class Pgm(object):

    '''
    PgmAbstract is an abstract class of the command program in facebook bot. 
    Subclass must define the functions to execute / check valid command function
    / enum of the state in each state of the program. 

    '''

    #__metaclass__ = abc.ABCMeta
    
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


    

