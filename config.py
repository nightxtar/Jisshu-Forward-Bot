# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "15257211")
    API_HASH = environ.get("API_HASH", "8b7cf73ce577720d74a213bbb98f4104")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6171845618:AAFn1Lu0OKZ06CFZjrcjgwBG_aLxW3n3fLA") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1350212613').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://AMMAAAAA:AMMAAAAA@cluster0.mi7ldio.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "zia")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001583883335'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1001940661697") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
