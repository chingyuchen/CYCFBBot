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

from pgm import Pgm
import msganalyzer
import requests
import messenger

################################################################################

class Default(Pgm):
    
    ''' 
    "/default" command program. Ask the user to choose between provided options
    (in buttons), then use the respond message as the argument to execute the 
    next state function of the program. The default program is the standby 
    running program.
    '''

#-------------------------------------------------------------------------------

    def state_start(self, user, msg_content=None, args=None):
        
        '''
        The start state function. Return enum of the next state function and args. 
        '''

        buttons = [{"type":"postback", "title":"Opt1", "payload":"Opt1"},
                    {"type":"postback", "title":"Opt2", "payload":"Opt2"}]
        text = "Please choose an option"
        messenger.send_buttons(user, text, buttons)

        return ["RESPOND", args]

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

    def state_respond(self, user, msg_content=None, args=None):

        '''
        The respond state function. Return enum of the end state function and args.
        '''
        
        quick_replies = [
            {
                "content_type":"text",
                "title":"Quick1",
                "payload":"Quick1"
            },
            {
                "content_type":"text",
                "title":"Quick2",
                "payload":"Quick2"
            },
            {
                "content_type":"location"
            }
        ]

        messenger.send_quickreply(user, "Please choose quick option", quick_replies)
        
        return ["QUICKRESPOND", args]
        

#-------------------------------------------------------------------------------    

    def check_quickrespond(self, data):

        '''
        Return true if the respond message for the request state function from 
        the user is valid. Otherwise, return false.
        '''

        [chat_id, msg_type, msg_content] = msganalyzer.glance_msg(data)
        
        if msg_type is 'sent_msg': 
            if 'text' in msg_content:
                if msg_content['text'] == 'Quick1' or msg_content['text'] == 'Quick2':
                    return True
                else:
                    return False
            elif 'attachments' in msg_content and msg_content['attachments'][0]['type'] == 'location':
                return True
            else:
                return False
        else:
            return False

#-------------------------------------------------------------------------------

    def state_quickrespond(self, user, msg_content=None, args=None):

        '''
        The respond state function. Return enum of the end state function and args.
        '''
        if 'text' in msg_content:
            messenger.send_text(user, "Your option is {option}, end execution!".format(\
                option=msg_content['text']))
        else:
            messenger.send_text(user, "Got your location!")

        return ["END", None]

#-------------------------------------------------------------------------------    

    def __init__(self):

        '''
        The Default Class is initialized so the command execution will be operated 
        by the bot object (pymessenger.bot Bot object) initiated in 
        superclass. Each state corresponding execute function and check function 
        are specified.
        '''

        super().__init__("/default")

        self.statefun = {
                "START" : self.state_start, 
                "RESPOND" : self.state_respond,
                "QUICKRESPOND": self.state_quickrespond
        }

        self.check_cmd = {
                "START" : self.check_start, 
                "RESPOND": self.check_respond,
                "QUICKRESPOND" : self.check_quickrespond
        }
        

################################################################################

if __name__ == "__main__":
    
    ''' 
    For testing
    '''
   
    user = input("type user id : ")
    default_class = Default()
    default_class.state_start(user)
    default_class.state_respond(user)

