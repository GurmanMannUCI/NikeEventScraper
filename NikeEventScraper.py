#-Scrapes Nike event pages to see the name of the event.
#-Waits 6 seconds checking next webpage to not get IP banned.
#-Prints out name of event and writes it into main corpus.
#-Checks event names from corpus to determine which pages are 
#   worth rechecking to ensure nothing has changed

import requests
from unidecode import unidecode
from ReadAndWrite import Reader,Writer
import time

#ListOfNums is a list containing variants of webpages that are set to be scraped
ListOfNums = []

def Updater():
    '''Looks at main corpus to see which event pages were empty, to recheck
    them to ensure that the name of the pages hasn't changed. Adds variant of
    unnamed webpages to ListOfNums to be rechecked'''
    print("Checking to see which events were empty and are getting rechecked")
    for num,name in MasterDict.iteritems():
        if name == "No Event Scheduled":
            ListOfNums.append(num)
    print("Rechecking complete")

def NewLinkChecks(start,num):
    '''Checks to see if webpage being checked hasn't already been checked.
    If the webpage hasnt been checked, its variant is added to the ListOfNums to
    be checked'''
    for i in range(int(start),int(num)+1):
        if str(i) not in MasterDict.keys():
            ListOfNums.append(str(i))
    print("List of numbers to check completed")

def SortList():
    '''Returns sorted list of numbers, so that they can be checked and written
    in the text file in order'''
    return sorted(ListOfNums)

def EventChecker(num):
    '''Opens Nike Webpage with specific variant ID to read name of event. If
    no event is listed on the event webpage, its name is set to 'No Event Scheduled'
    , but if there is an event listed, its corresponding name is given to its variant ID'''
    r = requests.get("https://www.nike.com/events-registration/series?id={}".format(num))
    makefile = open("filename.txt",'wb')
    temptext = unidecode(r.text)
    makefile.write(temptext)
    readfile = open("filename.txt",'r' )
    for i in readfile.readlines():
        if '"name"' in i:
            splitfile = i.split('"')
            name  = (splitfile[5])
    if name == "name":
        name = "No Event Scheduled"
    print("CHECKING EVENT {} : {}".format(num,name))
    MasterDict[num] = name

    
def Setup(start,end):
    '''Initial Set up for Event scraper. Reads information from Corpus, updates
    list of numbers to be checked, and sorts list of numbers so they're ready to
    be checked'''
    global MasterDict
    MasterDict = Reader("MasterFile.txt")
    Updater()
    NewLinkChecks(start,end)
    ListOfNums = SortList()
    print("Setup steps ending")
    

def Main():
    '''Checks event pages for each number in ListOfNums, and then updates
    the main corpus file after 10 pages have been read. Waits 6 seconds before
    checking next page to avoid being IP banned from webpage.'''
    WriterNumber = 0
    for i in ListOfNums:
        time.sleep(6)
        try:
            EventChecker(i)
            WriterNumber += 1
        except:
            print("ERROR AT {}".format(i))
            break
        if WriterNumber == 10:
            Writer("MasterFile.txt",MasterDict)
            WriterNumber = 0
    Writer("MasterFile.txt",MasterDict)
    print("DONE")

if __name__ == "__main__":
    '''Sets up Module. Set so that Event Scraper will only run
    if this module is the main file ran. Allows for other modules to
    use functions from this module.'''
    Setup(0,10000)
    Main()
