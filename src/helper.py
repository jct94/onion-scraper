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

#Initiating connectiom
with Controller.from_port(port=9051) as controller:
    controller.authenticate("16:404611117881919D60FDE86DEE8A97B9C744F0D35E5D2E96DF6C04C71E")
    controller.signal(Signal.NEWNYM)

#TOR-Config
SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc is configured to
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket

#DNS-Resolution
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo


#Scrapping Onion links.
def scrape(url, timeout_value = 10):
    """
    Core function : Scrape URL HTML content using bs4
    -------------------------------------------------
    url : onion hidden service
    timeout : default value 60000ms - can be bigger for onion services
    """
    timeout = timeout_value
    socket.setdefaulttimeout(timeout)

    #collecting html content.
    headers = {'User-Agent': 'Onion services scrapper | github.com/jct94/TorScrapper.git' }
    req = urllib.request.Request(url,data = None, headers)
    response = urllib.request.urlopen(req)

    #load response - print some info
    content = response.read()
    #try:
    #    print("Response has a length of {}".format(len(content)))
    #except ValueError:
    #    print("Not a valid input : go ahead")

    #parse html response
    page = BeautifulSoup(content,'html.parser')

    #output id
    id = re.sub(r'[^\w]', '', url)
    name = os.path.abspath("") + '/output/scraped-' + id + '.txt'
    #output saving
    file = open(name,'w')
    file.write(str(page.text))
    file.close()

if __name__=='__main__':

    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv)==2:
        url=sys.argv[1]
        try:
            scrape(url)
        except ValueError:
            print("Invalid input")
