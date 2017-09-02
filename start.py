################################################################################
'''
File: start.py
Author: Ching-Yu Chen

Description:
start.py contains Start class, which is a program object of the "/start" command
for the facebook bot.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import abc
from pgmabstract import PgmAbstract     
import fbmq
from fbmq import Page
from pymessenger.bot import Bot

################################################################################

class Start(PgmAbstract):

    ''' 
    "/start" command program. Send greeting message. 
    '''

    name = "/start"

    # enum of the state of the program

    START = 0
    END = -1

#-------------------------------------------------------------------------------

    def check_start(self, data):
        return True

#-------------------------------------------------------------------------------

    def state_start(self, user, msg_content=None, args=None):

        '''
        The start state function. Send greeting to the user and return enum 
        of the end state function. args provide the user name.
        '''

        user_profile = self.page.get_user_profile(user)
        name = user_profile["first_name"]

        self.bot.send_text_message(user, 'Hi, {first_name}! this is start program.'\
            ' Please type /help for commands instruction.'.format(first_name=name))

        return [Start.END, None]

#-------------------------------------------------------------------------------
        
    def __init__(self):
        
        '''
        The Start Class is initialized so the command execution will be operated 
        by the bot object (pymessenger.bot Bot object) initiated in 
        superclass. Each state corresponding execute function and check function 
        are specified.
        '''
        
        try:
            TOKEN = ""
            with open('Token', 'r') as f:
                TOKEN = f.read().strip()
                f.close()
                assert(len(TOKEN) != 0)
        except:
            print("Token file doesn't exit or invalid token")

        self.page = fbmq.Page(TOKEN)

        self.statefun = [self.state_start]
        self.check_cmd = [self.check_start]
        super().__init__()

################################################################################

if __name__ == "__main__":
    
    '''
    For testing
    '''

    startclass1 = Start()
