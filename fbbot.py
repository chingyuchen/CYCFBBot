################################################################################
'''
File : fbbot.py
Author: Ching-Yu Chen

Description:
fbbot.py is a facebook bot communicate with facebook users and execute commands.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

from flask import Flask, request
from pymessenger.bot import Bot
import requests
from cmdanalyzer import CmdAnalyzer
import msganalyzer
import fbmq
from fbmq import Page
import cmdlibrary

################################################################################

try:
    TOKEN = ""
    with open('Token', 'r') as f:
        TOKEN = f.read().strip()
    f.close()
    assert(len(TOKEN) != 0)
except:
    print("Token file doesn't exit or invalid token")
 
# object send message to user
bot = Bot(TOKEN)

# bot id
botid = fbmq.Page(TOKEN).page_id

# Flask object
app = Flask(__name__)

# object analyzes if the command from the user is valid.
cmd_analyzer = CmdAnalyzer()

#
portnum = 5000

#
invalidmsg = 'Not a valid command. Please retype the command or type /help for'\
' command instructions.'

################################################################################

@app.route('/', methods=['POST'])
def handle_incoming_messages():

    '''
    Handle the recieved message. If the message is a valid command then execute
    the command. Otherwise, send user an error message.
    '''
    
    data = request.json
    [chat_id, msg_type, msg_content] = msganalyzer.glance_msg(data)

    if chat_id == botid:
        return "ok"

    if msg_type is not 'state':
        if cmd_analyzer.is_command(data): 
            cmd_analyzer.execute(chat_id, msg_content)
        else:
            bot.send_text_message(chat_id, invalidmsg)
        
    else:
        pass

    return "ok"

################################################################################

def set_port(num):
    global portnum
    portnum = num 

#-------------------------------------------------------------------------------

def get_port():
    global portnum
    return portnum

#-------------------------------------------------------------------------------

def set_invalid_cmd_msg(msg):
    if type(msg) is str:
        global invalidmsg
        invalidmsg = msg
    else:
        raise TypeError("Invalid command message must be string")

#-------------------------------------------------------------------------------

def run():

    ''' 
    Starts running the bot
    '''
    app.run(port=portnum, debug=True)

#-------------------------------------------------------------------------------

def add_cmdpgm(pgmcmd):
    if type(pgmcmd) is str:
        cmdlibrary.add_cmdpgm(pgmcmd)
    else:
        raise TypeError("Command of the new program must be string")

#-------------------------------------------------------------------------------

def get_pgmcmds():
    return cmdlibrary.command_library.keys()

#-------------------------------------------------------------------------------

def get_pgmstates(pgmcmd):
    return cmdlibrary.get_pgmstates(pgmcmd)

#-------------------------------------------------------------------------------

def remove_cmdpgm(pgmcmd):
    if type(pgmcmd) is str:
        if pgmcmd in cmdlibrary.command_library:
            if pgmcmd == "/start" or pgmcmd == "/default":
                raise ValueError("/start and /default programs can't be removed")
            else: 
                cmdlibrary.remove_cmdpgm(pgmcmd)
        else:
            raise ValueError("program doesn't exist")
    else:
        raise TypeError("Command of the program must be string")

#-------------------------------------------------------------------------------

def add_pgm_state(pgmcmd, statename, check_cmd_function, state_function):
    # check if function returns state
    # should use another function to help user create state function
    if statename is None or check_cmd_function is None or state_function is None:
        raise ValueError("Input arguments can't be None")
    elif pgmcmd not in cmdlibrary.command_library:
        raise ValueError("Program doesn't exist. Use add_cmdpgm add the pgm first.")
    else:
        cmdlibrary.add_pgm_state(pgmcmd, statename, check_cmd_function, \
            state_function)

#-------------------------------------------------------------------------------

def set_pgm_state(pgmcmd, statename, check_cmd_function=None, state_function=None):

    if statename is None or (check_cmd_function is None and state_function is None):
        raise ValueError("Input arguments can't be None")
    elif pgmcmd not in cmdlibrary.command_library:
        raise ValueError("Program doesn't exist. Use add_cmdpgm add the pgm first.")
    else:
        cmdlibrary.set_pgm_state(pgmcmd, statename, check_cmd_function, \
            state_function)

#-------------------------------------------------------------------------------

def remove_pgm_state(pgmcmd, statename):
    if type(pgmcmd) is not str or type(statename) is not str:
        raise TypeError("arguments must be string")
    elif pgmcmd not in cmdlibrary.command_library:
        raise ValueError("Program doesn't exsit, Use add_cmdpgm add pgm first.")
    elif statename == "START":
        raise ValueError("START state can't be removed")
    else:
        cmdlibrary.remove_pgm_state(pgmcmd, statename)

################################################################################

if __name__ == '__main__':

    '''
    For testing
    '''
    run()
