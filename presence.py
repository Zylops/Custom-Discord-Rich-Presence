from pypresence import Presence
import time

client_id = input('Enter your client ID: ')
stt = input('Enter the state of your application: ')
dtls = input('Enter a description: ')
limg_id = input("Enter the ID of your large image: ")
simg_id = input("Enter the ID of your small image: ")
limg_desc = input("Enter the description of your large image: ")

RPC = Presence(client_id)
RPC.connect()

print(RPC.update(state=stt, details=dtls, large_image=limg_id, small_image=simg_id, large_text=limg_desc, start=time.time()))  # Set the presence

while True:
    time.sleep(15)
