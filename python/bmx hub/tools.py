import os
import time
def lateral_fade(string="later fade", timex=0.02):
    str_list = []
    aux = 0
    for _ in range(len(string)):
        time.sleep(timex)
        os.system("clear")

        str_list.append(string[aux])
        if len(str_list) % 2 == 0:
            print("".join(str_list)+"_")
        if not len(str_list) % 2 == 0:
            print("".join(str_list))
        aux += 1