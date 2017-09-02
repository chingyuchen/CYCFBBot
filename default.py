################################################################################
'''
File: default.py
Author: Ching-Yu Chen

Description:
default.py contains Default class, which is a program object of the "/default" 
command. Default pgm is the standby running program.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import abc
from pgmabstract import PgmAbstract
from pymessenger.bot import Bot
import msganalyzer

################################################################################

class Default(PgmAbstract):
    
    ''' 
    "/default" command program. Ask the user to choose between provided options
    (in buttons), then use the respond message as the argument to execute the 
    next state function of the program. The default program is the standby 
    running program.
    '''

    name = "/default"
    

    # enum of the state of the program

    START = 0
    RESPOND = 1
    END = -1


#-------------------------------------------------------------------------------

    def check_start(self, data=None):
        return True

#-------------------------------------------------------------------------------

    def state_start(self, user, msg_content=None, args=None):
        
        '''
        The start state function. Return enum of the next state function and args. 
        '''

        buttons = [{"type":"postback", "title":"Opt1", "payload":"Opt1"},
                    {"type":"postback", "title":"Opt2", "payload":"Opt2"}]
        text = "Please choose an option"
        self.bot.send_button_message(user, text, buttons)

        return [Default.RESPOND, args]

#-------------------------------------------------------------------------------

    def check_respond(self, data):

        '''
        Return true if the respond message for the request state function from 
        the user is valid. Otherwise, return false.
        '''

        [chat_id, msg_type, msg_content] = msganalyzer.glance_msg(data)
        
        if msg_type is 'postback':
            if msg_content['title'] == 'Opt1' or msg_content['title'] == 'Opt2':
                return True
            else:
                return False
        else:
            return False

#-------------------------------------------------------------------------------

    def state_respond(self, user, msg_content, args=None):

        '''
        The respond state function. Return enum of the end state function and args.
        '''

        '''
        code implemented here
        '''
        
        return [Default.END, args]
        

#-------------------------------------------------------------------------------    
    
    def __init__(self):

        '''
        The Default Class is initialized so the command execution will be operated 
        by the bot object (pymessenger.bot Bot object) initiated in 
        superclass. Each state corresponding execute function and check function 
        are specified.
        '''

        self.statefun = [self.state_start, self.state_respond]
        self.check_cmd = [self.check_start, self.check_respond]
        super().__init__()
        

################################################################################

if __name__ == "__main__":
    
    ''' 
    For testing
    '''
   
    default_class = Default()

