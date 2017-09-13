import requests
import json

try:
    TOKEN = ""
    with open('Token', 'r') as f:
        TOKEN = f.read().strip()
        f.close()
        assert(len(TOKEN) != 0)
except:
    print("Token file doesn't exit or invalid token")


urlS = "https://graph.facebook.com/v2.6/me/messages?access_token="

#-------------------------------------------------------------------------------

def send_text(user, text=None):
    data = {
                "recipient": {"id": user},
                "message": {
                    "text": text,
                }
            }
    
    resp = requests.post(urlS + TOKEN, json=data)
    

#-------------------------------------------------------------------------------

def send_quickreply(user, text=None, quick_replies=None):
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

def get_page_info():
    resp = requests.get("https://graph.facebook.com/v2.6/me",
                        params={"access_token": TOKEN},
                        headers={'Content-type': 'application/json'})

    info = json.loads(resp.text)
    return info 

#-------------------------------------------------------------------------------

def get_user_info(user):
    resp = requests.get("https://graph.facebook.com/v2.6/%s" % user,
                        params={"access_token": TOKEN},
                        headers={'Content-type': 'application/json'})

    info = json.loads(resp.text)
    return info
    
