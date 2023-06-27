from pynput.keyboard import Listener

def on_press(key):
	val = True
	if key.replace('', "") == "return.key":
		val = False
	while val:
		with Listener(on_press=on_press) as ls:
			ls.join()



