################################################################################

def isState(entry):
    if 'messaging' not in entry:
        return True 
    else:
        messaging = entry['messaging'][0]
        if 'postback' in messaging or 'message' in messaging:
            return False 
        else:
            return True 



def glance_msg(data):

    entry = data['entry'][0]
    if isState(entry):
        msg_type = 'state'
        msg_content = None
        chat_id = None
        return [chat_id, msg_type, msg_content] 
    else:
        messaging = entry['messaging'][0]
        chat_id = messaging['sender']['id']
        if 'message' in messaging:
            msg_content = messaging['message']
            msg_type = 'sent_msg'
        elif 'postback' in messaging:
            msg_content = messaging['postback']
            msg_type = 'postback'
        else:
            msg_content = None
            msg_type = 'unknown'
        return [chat_id, msg_type, msg_content]

