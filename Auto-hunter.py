import sys
import re 
import docx2txt
import time
import pyfiglet
import requests
import base64
import json
import os
import webbrowser
import xmltodict

def readfile(fileName):
    f = open(fileName)
    listItems = f.read().splitlines()
    return listItems

def ipgrabber(fileName):
    rpf = open("hunter_ip.txt", "w")
    listing = []
    for line in readfile(fileName):
        for matach in re.findall(ipgrabber,line):
            if '.gov' in match:
                continue
            if matach not in listing:
                listing.append(match)
                print(matach,file=rpf)
    
    if listing == []:
        print("")
        print("===========================")
        print(" No IP Addresses in report ")
        print("===========================")
    else:
        print("")
        print("=======================================================")
        print(" Grabbing IP Addresses ")
        print(" Retrieved IP Address can be viewed in 'hunter_ip.txt' ")
        print("=======================================================")
        for item in listing:
            print(item)
    print("")
    print("Checking if IP Address are Blocked on the network")
    for item in listing:
        proxyBlockcheck(item)



def emailgrabber(fileName):
    rpf = open("hunter_emails.txt", "w")
    listing = []
    for line in readfile(fileName):
        for match in re.findall(EmailPattern, line):
            if '.gov' in match:
                continue
            if match not in listing:
                listing.append(match)
                print(match, file=rpf)
    
    if listing == []:
        print("")
        print("===========================")
        print(" No IP Addresses in report ")
        print("===========================")
    else:
        print("")
        print("=======================================================")
        print(" Grabbing IP Addresses ")
        print(" Retrieved IP Address can be viewed in 'hunter_email.txt' ")
        print("=======================================================")
        for item in listing:
            print(item)
    
def urlgrabber(fileName):
    rpf = open("hunter_url.txt", "w")
    listing = []
    for line in readfile(fileName):
        for match in re.findall(URLPattern, line):
            if '.gov' in match:
                continue
            if match not in listing:
                listing.append(match)
                print(match, file=rpf)
    
    if listing == []:
        print("")
        print("===========================")
        print(" No URL's in report ")
        print("===========================")
    else:
        print("")
        print("=======================================================")
        print(" Grabbing URL's ")
        print(" Retrieved URL's can be viewed in 'hunter_url.txt' ")
        print("=======================================================")
        for item in listing:
            print(item)
    print("")
    print("Checking if URL's are blocked on the network")
    for item in listing:
        proxyBlockcheck(item)

def sha256grabber(fileName):
    rpf = open("hunter_SHA256.txt", "w")
    listing = []
    for line in readfile(fileName):
        for match in re.findall(SHA256hashpattern,line):
            if '.gov' in match:
                continue
            if match not in listing:
                listing.append(match)
                print(match, file=rpf)
    if listing == []:
        print("")
        print("===========================")
        print(" No SHA256 Hashes in report ")
        print("===========================")
    else:
        print("")
        print("=======================================================")
        print(" Grabbing SHA256 Hashes ")
        print(" Retrieved SHA256 Hashes can be viewed in 'hunter_SHA256.txt' ")
        print("=======================================================")
        for item in listing:
            print(item)

def iocGrabber(fileName):
    ipgrabber(fileName)
    emailgrabber(fileName)
    sha256grabber(fileName)
    urlgrabber(fileName)

def fileCleanup():
    sha256fsize = os.path.getsize("hunter_SHA256.txt")
    urlfsize = os.path.getsize("hunter_url.txt")
    ipfsize = os.path.getsize("hunter_ip.txt")
    emailfsize = os.path.getsize("hunter_emails.txt")

    if sha256fsize == 0:
        os.remove("hunter_SHA256.txt")
    if urlfsize == 0:
        os.remove("hunter_url.txt")
    if ipfsize == 0:
        os.remove("hunter_ip.txt")
    if emailfsize == 0:
        os.remove("hunter_emails.txt")
