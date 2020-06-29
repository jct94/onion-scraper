import sys
import re
import os

import urllib.request

#scraping library
from bs4 import BeautifulSoup


#Tor connection protocol - stem lib
from stem import Signal
from stem.control import Controller

import socks
import socket

#Initiating Connection
with Controller.from_port(port=9051) as controller:
    controller.authenticate("16:404611117881919D60FDE86DEE8A97B9C744F0D35E5D2E96DF6C04C71E")
    controller.signal(Signal.NEWNYM)

# TOR SETUP GLOBAL Vars
SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc is configured to
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket

# Perform DNS resolution through the socket
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

#######################################################################################################################
################################################ TOR CONNECTION ABOVE #################################################
#######################################################################################################################

#Scrapping Onion links.
def Scrape(url):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    #Collecting html content.
    headers = {'User-Agent': 'TorScrapper - Onion scrapper | github.com/ConanKapoor/TorScrapper.git' }
    req = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(req)

    #Using BeautifulSoup to parse html object response.
    page = BeautifulSoup(response.read(),'html.parser')

    #Saving output
    token = re.sub(r'[^\w]', '', url)
    name = os.path.abspath("") + '/Output/Scraped-' + token +'.html'
    file = open(name,'w')
    file.write(str(page))
    file.close()

# Taking input.
if __name__=='__main__':
    if (len(sys.argv)==2):
        url=sys.argv[1]
        Scrape(url)
    else:
        print("Invalid input")
