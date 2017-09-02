################################################################################
'''
File: help.py
Author: Ching-Yu Chen

Description:
help.py contains Help class, which is a program object of the "/help" command. 
Help pgm send the commands instruction to the users.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import abc
from pgmabstract import PgmAbstract     
from pymessenger.bot import Bot

################################################################################

class Help(PgmAbstract):

    ''' 
    "/help" command program. Send information of the commands to the user.
    '''
    
    name = "/help"
    

    # enum of the state of the program

    START = 0
    END = -1

#-------------------------------------------------------------------------------

    def check_start(self, data):
        return True

#-------------------------------------------------------------------------------

    def state_start(self, user, msg_content=None, args=None):

        '''
        The inform state function. Send commands instruction to the users and
        return the enum of the end state.
        '''

        self.bot.send_text_message(user, \
            '/default : default program.\n'
            '/start : start program\n'
            '/help : help program')

        return [Help.END, None]

#-------------------------------------------------------------------------------
        
    def __init__(self):
        
        '''
        The Help Class is initialized so the command execution will be operated 
        by the bot object (pymessenger.bot Bot object) initiated in 
        superclass. Each state corresponding execute function and check function 
        are specified.
        '''

        self.statefun = [self.state_start]
        self.check_cmd = [self.check_start]
        super().__init__()

#-------------------------------------------------------------------------------

if __name__ == "__main__":

    '''
    For testing
    '''
    helpclass = Help()
