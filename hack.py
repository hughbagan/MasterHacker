# 1337 MASTER HAX 42069
import random
import time

def init_hacks():
    functions = [
        "VOID HACK_MAINHACK("+str(random.randint(9999999,100000000)),
        "INT BREAK_CODE(MAINFRAME)",
        "INT* BREAK_LOCK(IP_ADDRESS)",
        "VOID LOCATE_GEOIP(IP_ADDRESS)",
        "VOID KILL_CHILD(ROOT.CHILDREN)",
        "VOID FIND_PARENT(NODE)"
    ]
    expressions = [
        "PRINTF('MASTERHAXOR');",
        "TARGET = MAX(IP_DATABASE;",
        "NUKE_CODES = GEO_GET(IPBASE.WHITE_HOUSE);",
        "LAUNCH_NUKES();"
    ]
    comments = [
        "# CRACKING VAULT CODES",
        "# CRACKING VAULT CODES",
        "# BYPASSING 128-BIT ENCRYPTION",
        "# ACCESSING METASPLOIT API",
        "# TAPPING INTO WIRESHARK",
        "# 070 117 099 107"
    ]
    return (functions, expressions, comments)

def spam():
    chars = ['$','%','#','1','2','3','.','4','5','6','7','8','9','0']
    num_chars = random.randint(0,500)
    for i in range(0,num_chars):
        print(chars[random.randint(0,len(chars)-1)], end='', flush=True)
        time.sleep(0.005)
    time.sleep(0.20)

def main():
    hax_spd = 0.04

    # Initialize strings
    functions, expressions, comments = init_hacks()
    print('\n'+ "$"*30 + " COMMENCING HACK " +"$"*30+'\n')
    time.sleep(0.5)

    # Enter haxor loop
    while(True):
        # Print out the haxxor line
        if (random.random() < 0.3):
            print(comments[random.randint(0, len(comments)-1)])
        func = functions[random.randint(0,len(functions)-1)]
        print(func+ ' {')
        for i in range(0,50):
            expr = expressions[random.randint(0, len(expressions)-1)]
            if (random.random() < 0.3):
                print('\t'+comments[random.randint(0,len(comments)-1)])
            if (random.random() < 0.05):
                spam()
            else:
                print('\t'+expr)
                if (random.random() < 0.5):
                    # Indent the haxxxxx!!
                    for i in range(0,20):
                        expr = expressions[random.randint(0, len(expressions)-1)]
                    print('\t\t'+expr)
            time.sleep(0.10)
        if (random.random() < hax_spd):
            spam()
        print('}' +'\n')
        time.sleep(hax_spd)

main()
