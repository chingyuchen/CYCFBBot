################################################################################
'''
File : messenger.py
Author: Ching-Yu Chen

Description:
The messenger module includes methods of sending different type of message from
the facebook messenger bot to the users.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import requests
import json

################################################################################

# geocoder key
key = ""
try:
    with open('geocoder_key', 'r') as f:
        key = f.read().strip()
        f.close()
    assert(len(key) != 0)
except:
    print("error in accessing geocoder key")


# Token of the bot
try:
    TOKEN = ""
    with open('Token', 'r') as f:
        TOKEN = f.read().strip()
        f.close()
        assert(len(TOKEN) != 0)
except:
    print("Token file doesn't exit or invalid token")


# url of post
urlS = "https://graph.facebook.com/v2.6/me/messages?access_token="

################################################################################

def send_text(user, text=None):
    
    '''
    Send text message to the user
    '''

    data = {
                "recipient": {"id": user},
                "message": {
                    "text": text,
                }
            }
    
    resp = requests.post(urlS + TOKEN, json=data)
    

#-------------------------------------------------------------------------------

def send_quickreply(user, text=None, quick_replies=None):

    ''' 
    Send quick reply message to the user, with text and quick_replies option.
    '''

    data = {
                "recipient": {"id": user},
                "message": {
                    "text": text,
                    "quick_replies":quick_replies,
                }
            }
    
    resp = requests.post(urlS + TOKEN, json=data)

#-------------------------------------------------------------------------------

def send_buttons(user, text, buttons):

    '''
    Send button messgae to the user, with text and buttons.
    '''

    data = {
                "recipient": {"id": user},
                "message": {
                    "attachment":{
                        "type": "template", 
                        "payload":{
                            "template_type": "button", 
                            "text":text,
                            "buttons":buttons
                        }
                    }
                }

            }

    resp = requests.post(urlS + TOKEN, json=data)

#-------------------------------------------------------------------------------

def send_location(user, lat, lon):

    '''
    Send location message to the user, according to the lat and lon.
    '''

    # check arguments
    imageurl = "https://maps.googleapis.com/maps/api/staticmap?key=" + key +\
        "&markers=color:red|label:B|" + str(lat) + "," + str(lon) + "&size=360x360&zoom=13"
    itemurl = "http://maps.apple.com/maps?q="+ str(lat) +","+ str(lon) +"&z=16"

    data = {
                "recipient": {"id": user},
                "message": {
                    "attachment":{
                        "type": "template", 
                        "payload":{
                            "template_type":"generic",
                            "elements":{
                                "element":{
                                    "title": "Tab to open map",
                                    "image_url":imageurl,
                                    "item_url":itemurl
                                }
                            }
                        }
                    }
                }
            }

                                    #"item_utl":itemurl
    resp = requests.post(urlS + TOKEN, json=data)

#-----------------------------------------------------------------------

def get_page_info():

    '''
    Get page info.
    '''

    resp = requests.get("https://graph.facebook.com/v2.6/me",
                        params={"access_token": TOKEN},
                        headers={'Content-type': 'application/json'})

    info = json.loads(resp.text)
    return info 

#-------------------------------------------------------------------------------

def get_user_info(user):

    '''
    Get user info.
    '''

    resp = requests.get("https://graph.facebook.com/v2.6/%s" % user,
                        params={"access_token": TOKEN},
                        headers={'Content-type': 'application/json'})

    print("resp = " + str(resp))
    info = json.loads(resp.text)
    return info


#########################################################################

if __name__ == "__main__":

    '''
    For testing
    '''

    user = input("enter user:") 
    send_text(user, "hi")
    send_location(user, 40, 70)
    
