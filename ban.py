from pyrogram import Client
import time


ID = "3147700"
HASH = "e660ea4d20e70a3897aa8cf3a6dc60af" 
SESS = str(input("\n Send Pyrogram V2 session: "))

RiZoeL = Client("RiZoeL", api_id=ID, api_hash=HASH, session_string=SESS)

grp = int(input("Enter Group id: "))

try:
   RiZoeL.start()
   for x in RiZoeL.get_chat_members(grp):
       user = x.user
       try:
          RiZoeL.ban_chat_member(grp, user.id)
          time.sleep(0.01)
          print("Banned {user.first_name}")
       except Exception as a: 
         print(a)
         continue
except Exception as a:
    print(a)
