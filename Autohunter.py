import time
import sys
import pyfiglet
from ADFunc import ADlookup

def exit_tool():
    sys.exit()

def PrintBanner():
    result = pyfiglet.figlet_format("AUTO - HUNTER", font = "SLANT")
    print(result)

def menu():
    print("===============================================================================")
    print("|                            Available Options:                               |")
    print("===============================================================================")
    print("|    -0-     | AD info                                                        |")
    print("|    -1-     | Site Review (Zscaler)                                          |")
    print("|    -2-     | URL Analysis                                                   |")
    print("|    -3-     | Proxy Check                                                    |")
    print("|    -4-     | Mailbox Check                                                  |")
    print("|    -5-     | SSH                                                            |")
    print("|    -7-     | Exit                                                           |")
    print("===============================================================================")
    
    try:
        i = input("Select available option: ")
        if i == '0':
            ADlookup()
        if i == '1':
            print("Nonethin yet")
        if i == '2':
            print("Nonethin yet")
        if i == '3':
            print("Nonethin yet")
        if i == '4':
            print("Nonethin yet")
        if i == '5':
            print("Nonethin yet")
        if i == '6':
            print("Nonethin yet")
        if i == '7':
            exit_tool()
        else:
            time.sleep(0.5)
            menu()
    except:
        exit_tool()

if __name__ == '__main__':
    PrintBanner()
    menu()

