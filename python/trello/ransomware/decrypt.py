from cryptography.fernet import * 
from tkinter import messagebox

#opens file w/key and saves it in a var
with open("key.txt", "rb") as filekey:
	key = filekey.read()

#reads encrypted file
with open("target.txt", "rb") as enc_file:
	encrypted = enc_file.read()

#saves decrypted content in a var
decrypted = Fernet(key).decrypt(encrypted)

#decrypts file
with open("target.txt", "wb") as dec_file:
	dec_file.write(decrypted)
	messagebox.showinfo("oh yes", "target.txt has been decrypted")

#dels key.txt
os.remove("key.txt")