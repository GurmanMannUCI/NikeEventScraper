#Used to read and write from the main corpus of information

def Reader(filename):
    '''Reads from the filename to pull information of already checked events'''
    MasterDict = dict()
    print("Attempting to open and read text from master file")
    try:
        mainfile = open(filename,'r')
        print("{} found".format(filename))
    except:
        print("{} couldnt be found. Continuing to next step".format(filename))
    else:
        try:
            print("Attempting to read from {}".format(filename))
            readfile = mainfile.readlines()
            for i in readfile:
                try:
                    splitline = i.split(':')
                    num = splitline[0].strip()
                    name = splitline[1].strip()
                    MasterDict[str(num)] = name
                except:
                    pass
        except:
            print("Read from {} failed. Continuing to next step".format(filename))
            pass
    return MasterDict

def Writer(filename,MasterDict):
    '''Writes into main corpus to ensure progress is saved, and corpus remains updated'''
    print("Writing Results into file")
    mainfile = open(filename,"w")
    for key,value in sorted(MasterDict.items(),key=lambda x:x[0]):
        mainfile.write("{} :    {}\n".format(key,value))
    print("Completed writing Results into file")
