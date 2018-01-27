# 1337 MASTER HAX 42069
import random
import time

def init_hacks():
    lines = [
            "ACCESSING CIA DATABASE",
            "HACKING THE GOVERNMENT"
            "DUMPED MCDONALDS"
            ]
    return lines

def main():
    hacks = init_hacks()
    print("$$$$$$$$$$$$$ COMMENCING HACK $$$$$$$$$$$$$$")
    while(True):
        line_ind = random.randint(0,len(hacks)-1)
        print(hacks[line_ind])
        time.sleep(0.25)

main()
