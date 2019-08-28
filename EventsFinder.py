#Goes through main corpus and pulls out only events that are scheduled

from ReadAndWrite import Reader,Writer

def EventListCreator():
    '''Checks to see which events have a non-default name'''
    for key,value in MasterDict.items():
        if value == "No Event Scheduled":
            del MasterDict[key]
    
if __name__ == "__main__":
    '''Creates a main dictionairy, and reads entire corpus into it.
    Parses through dictionairy to find keys key,value pairs that arent set
    as "No Event Scheduled" events. Outputs filtered dictionairy into seperate file'''
    global MasterDict
    MasterDict = Reader("MasterFile.txt")
    EventListCreator()
    Writer("ListOfFoundEvents.txt",MasterDict)
    print("Done")
