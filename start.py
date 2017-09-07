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

from pgm import Pgm     
import fbmq
from fbmq import Page
from pymessenger.bot import Bot

################################################################################

class Start(Pgm):

    ''' 
    "/start" command program. Send greeting message. 
    '''

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

        return ["END", None]

#-------------------------------------------------------------------------------
        
    def __init__(self):
        
        '''
        The Start Class is initialized so the command execution will be operated 
        by the bot object (pymessenger.bot Bot object) initiated in 
        superclass. Each state corresponding execute function and check function 
        are specified.
        '''
        
        super().__init__("/start")

        try:
            TOKEN = ""
            with open('Token', 'r') as f:
                TOKEN = f.read().strip()
                f.close()
                assert(len(TOKEN) != 0)
        except:
            print("Token file doesn't exit or invalid token")

        self.page = fbmq.Page(TOKEN)

################################################################################

if __name__ == "__main__":
    
    '''
    For testing
    '''
    user = input("type user id : ")
    startclass1 = Start()
    startclass1.state_start(user)
    startclass1.run(user, "START")
    
