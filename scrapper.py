import os

#multiprocess request
from multiprocessing import Pool

#nice figlet when running on terminal
from pyfiglet import Figlet

#onion.txt containing hidden services adresses
with open("onions.txt", "r") as onion:
    content = onion.read().splitlines()


def editor():
    """
    Add links to onions.txt using nano terminal text editor
    """
    command = "nano onions.txt"
    os.system(command)


def scraper_execution(url):
    """
    Command line emulator for scraping
    """
    execute = 'python3 src/helper.py + {}'.format(url)
    print(execute)
    try:
        os.system(execute)
    except:
        logging.error("Scraping failed")


#multiprocessing wrapper for execution
def multiprocessing(task, processes=10):
    """
    Multiprocessing wrapper
    Clear former output directory and create a new one
    --------------------------------------------------
    task : scraper_execution or editor
    processes : Number of URLs that will be processed at the same time
    """

    #output directory
    if (os.path.exists("output")):
        delete_command = str('rm -r output')
        os.system(delete_command)
        os.makedirs("output")
    else:
        os.makedirs("output")

    with Pool(processes) as pool:
        for onion in range(0, len(content)):
            pool.apply(task, args=(content[onion],))

#Program banner
def banner():
    banner = Figlet(font='slant')
    print (banner.renderText('TorScraper'))
    print ("\n")

#Program menu
def menu():
    print ("Please select one of the following options:- \n")
    print (" 1. Add links to onions.txt input file")
    print (" 2. Scrap hidden services present in onions.txt")
    print (" 3. Exit.\n")

if __name__ == '__main__':
    scrap_active = 1
    try:
        while(scrap_active):
            os.system("clear")
            banner()
            menu()
            choice = int(input("Choose one option: "))
            print("\n")

            if choice == 1:
                editor()
            elif choice == 2:
                multiprocessing(scraper_execution)
            else:
                scrap_active = 0
                quit()

    except KeyboardInterrupt:
        print("\n\nInterrupt received! Exiting cleanly...\n")
