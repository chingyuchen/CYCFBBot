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

#-------------------------------------------------------------------------------

app = Flask(__name__)

#-------------------------------------------------------------------------------

# object analyzes if the command from the user is valid.
cmdanalyzer = CmdAnalyzer()

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
        if cmdanalyzer.is_command(data): 
            cmdanalyzer.execute(chat_id, msg_content)
        else:
            bot.send_text_message(chat_id, 'Not a valid command. Please retype '
                'the command or type /help for command instructions.')
        
    else:
        pass

    return "ok"

#-------------------------------------------------------------------------------

def run():

    ''' 
    Starts running the bot
    '''

    app.run(debug=True)
 
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    '''
    For testing
    '''
    run()
    #app.run(debug=True)
