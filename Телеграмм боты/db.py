import  s_taper
from s_taper.consts import *
import random


scheme = {
    "userid": INT + KEY,
    "name": TEXT,
    "power": TEXT,
    "hp": INT,
    "dmg": INT,
    "lvl": INT,
    "xp": INT
}

users = s_taper.Taper('users', 'rpg.db').create_table(scheme)

heal_scheme = {
   "userid": INT + KEY,
   "food": TEXT
}

heals = s_taper.Taper("heals", "rpg.db").create_table(heal_scheme)

sleep_scheme = {
   "userid": INT + KEY,
   "seconds": INT
}

sleep = s_taper.Taper("sleep", "rpg.db").create_table(sleep_scheme)

defend_scheme = {
   "userid": INT + KEY,
   "score": INT
}

defend = s_taper.Taper("defend", "rpg.db").create_table(defend_scheme)

def is_new_player(msg):
    result = users.read_all()
    for user in result:
        if user[0] == msg.chat.id:
            return False
    return True
