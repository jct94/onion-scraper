# TorScrapper
A basic scrapper made in python with BeautifulSoup and Tor support to -

* Scrape Onion and normal links.
* Save the output in html format in Output folder.
* Filter the html output and strip out useful data only (Work in Progress).
* Striping out IOCs and other related data (On To-Do list).

## Basic setup
Before you run the torBot make sure the following things are done properly:

* Run tor service
`sudo service tor start`
or `brew service tor start` for MacOS user


* Set a password for tor
`tor --hash-password "my_password" `

* Modify value in scrapper.py

* Go to /etc/tor/torrc and uncomment - _**ControlPort 9051**_ , you may consider accessing torrc config file using `sudo nano torrc` to be able to save it


### Deployment

A step by step series of examples that tells what you have to do to get this project running -

* Enter the project directory.
* Copy all the onion and normal links you want to scrape in _onions.txt_

```
[nano]/[vim]/[gedit]/[Your choice of editor] onions.txt
```

* Run TorScrapper.py using Python3

```
[sudo] python3 TorScrapper.py
```

* Check the scraped outputs in Output folder.

# Tor Configuration

Look at your torrc for the following configuration options...

 Tor uses a text file called torrc that contains configuration instructions for how your Tor program should behave. The default configuration should work fine for most Tor users.

If you installed Tor Browser on Windows or Linux, look for Browser/TorBrowser/Data/Tor/torrc inside your Tor Browser directory. If you're on macOS, the torrc is in ~/Library/Application Support/TorBrowser-Data/Tor . To get to it, press cmd-shift-g while in Finder and copy/paste that directory into the box that appears.

Otherwise, if you are using Tor without Tor Browser, it looks for the torrc file in /usr/local/etc/tor/torrc if you compiled tor from source, and /etc/tor/torrc or /etc/torrc if you installed a pre-built package.

Once you've created or changed your torrc file, you will need to restart tor for the changes to take effect. (For advanced users, note that you actually only need to send Tor a HUP signal, not actually restart it.)

## torrc - Uncomment the following lines

ControlPort 9051
CookieAuthentication 1

#Alternatively we can authenticate with a password. To set a password first
#get its hash...
#
#% tor --hash-password "my_password"
#16:E600ADC1B52C80BB6022A0E999A7734571A451EB6AE50FED489B72E3DF
#
#... and use that for the HashedControlPassword in your torrc.

HashedControlPassword 16:E600ADC1B52C80BB6022A0E999A7734571A451EB6AE50FED489B72E3DF


## Built With

* [Python](https://www.python.org/) - Python programming language.
* [Tor](https://www.torproject.org/) - If you don't know about Tor then you probably shouldn't be here :)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Beautiful Soup is a Python library for pulling data out of HTML and XML files.
