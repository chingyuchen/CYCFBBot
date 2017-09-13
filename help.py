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

from pgm import Pgm     
import messenger

################################################################################

class Help(Pgm):

    ''' 
    "/help" command program. Send information of the commands to the user.
    '''

#-------------------------------------------------------------------------------

    def state_start(self, user, msg_content=None, args=None):

        '''
        The inform state function. Send commands instruction to the users and
        return the enum of the end state.
        '''

        messenger.send_text(user, \
            '/default : default program.\n'
            '/start : start program\n'
            '/help : help program')

        return ["END", None]

#-------------------------------------------------------------------------------
        
    def __init__(self):
        
        '''
        The Help Class is initialized so the command execution will be operated 
        by the bot object (pymessenger.bot Bot object) initiated in 
        superclass. Each state corresponding execute function and check function 
        are specified.
        '''

        super().__init__("/help")

#-------------------------------------------------------------------------------

if __name__ == "__main__":

    '''
    For testing
    '''

    user = input("type user id : ")
    helpclass = Help()
    helpclass.state_start(user)
