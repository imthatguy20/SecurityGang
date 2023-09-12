import subprocess
import time
import sys

def exit_tool():
    sys.exit()

def ADlookup():
    userName = input("Please provide UID: ")
    print("===============================================================================")
    print("|                            Available Options:                               |")
    print("===============================================================================")
    print("|    -1-     | All info                                                       |")
    print("|    -2-     | Last Bad Password Attempt                                      |")
    print("|    -3-     | Password Set                                                   |")
    print("===============================================================================")
try:
    i = input("Select available option: ")
    if i == '1':
        output = subprocess.run(['powershell.exe', "Get-ADUser -identity '" + userName +"' -properties *"], capture_output=True, text=True)
        print(output.stdout)
    if i == '2':
        output = subprocess.run(['powershell.exe', "Get-ADUser -identity '" + userName +"' -properties LastBadPasswordAttempt"], capture_output=True, text=True)
        print(output.stdout)
    if i == '3':
        output = subprocess.run(['powershell.exe', "Get-ADUser -identity '" + userName +"' -properties PasswordLastSet"], capture_output=True, text=True)
        print(output.stdout)
    else:
        time.sleep(0.5)
        ADlookup()
except:
    exit_tool()