################################################################################
'''
File: cmdanalyzer.py
Author: Ching-Yu Chen

Description:
cmdanalyzer.py contains a CmdAnalyzer class which is a object that analyzes the 
commands(messages) received from telegram user and able to execute the commands.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import json
import cmdlibrary 
import msganalyzer

################################################################################

user_state = {}
cmd_library = cmdlibrary.command_library 

################################################################################

class CmdAnalyzer:

    ''' 
    CmdAnalyzer analyzes the commands(messages) received from telegram user 
    and able to execute the command. It is initialized by given a bot (telepot 
    object) and a tb (telebot object)
    '''

    # the dict that maps the user to the current running program state
    #user_state = {}

#-------------------------------------------------------------------------------

    def __init__(self):

        # the dict that maps the commands to the program 
        #self._command_libarary = CmdLibrary().command_libarary 
        pass
        
#-------------------------------------------------------------------------------
    
    @staticmethod
    def intl_execute(userid, arg=None):

        ''' 
        The first function execute when starting a conversation with userid.
        It runs the "/start" cmd and then run the "/default" cmd.
        '''
        
        state_inform = {'cmd' : '/start', 'state' : 'START', 'arg' : arg}
        user_state[userid] = state_inform

#-------------------------------------------------------------------------------

    def is_command(self, data):

        ''' 
        Return True if a data is a valid cmd. Otherwise, return False.
        '''

        [chat_id, msg_type, msg_content] = msganalyzer.glance_msg(data)
        state_inform = user_state.get(chat_id, None)
        
        if state_inform is None:
            CmdAnalyzer.intl_execute(chat_id)
            return True

        if state_inform['check_cmd_fun'](data):  # check valid current pgm cmd
            if 'arg' not in state_inform:
                state_inform['arg'] = None
            return True

        elif msg_type != 'sent_msg' or 'text' not in msg_content:  # check valid new pgm cmd type
            return False
        
        else:
            commandi = msg_content['text']
            if commandi in cmd_library:  # check new pgm cmd
                state_inform['cmd'] = commandi
                state_inform['state'] = "START" 
                state_inform['check_cmd_fun'] = cmd_library[commandi].check_cmd["START"]
                state_inform['arg'] = None
                return True
            else:
                return False

#-------------------------------------------------------------------------------

    def execute(self, chat_id, msg_content=None):
        
        ''' 
        Execute the chat_id command
        '''

        state_inform = user_state.get(chat_id)
        classi = cmd_library[state_inform['cmd']]
        
        nextstate_info = \
        classi.run(chat_id, state_inform['state'], msg_content, state_inform['arg'])
        state_inform['state'] = nextstate_info[0]
        state_inform['arg'] = nextstate_info[1]  
        print("state_info = " + str(state_inform))

        if state_inform['state'] != "END": 
            state_inform['check_cmd_fun'] = \
            classi.check_cmd[state_inform['state']]

        if state_inform['state'] == "END": # pgm ends, run the default pgm
          
            classi = cmd_library['/default']
            state_inform['cmd'] = '/default'
            state_inform['state'] = "START" 
            state_inform['check_cmd_fun'] = \
            classi.check_cmd[state_inform['state']]

            nextstate_info = classi.run(chat_id, "START")
            
            state_inform['state'] = nextstate_info[0]
            state_inform['arg'] = nextstate_info[1]
            state_inform['check_cmd_fun'] = \
            classi.check_cmd[state_inform['state']]

        
################################################################################

if __name__ == "__main__":

    '''
    For testing
    '''

    testCmdAnalyzer = CmdAnalyzer()
