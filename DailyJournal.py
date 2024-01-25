from datetime import datetime 
filename = "Daily_Journal.txt"
def GetDate(): 
    t = datetime.now().strftime("%d%m%y")
    return "Date:" + t
def WelcomeMessage(): 
    print("****************************************\n")
    print("Welcome To Your Daily Journal Version.01\n")
    print("****************************************\n")


def SearchEntry():
    file = open(filename, "r") 
    f = input("Enter in a key word from an entry/entries you would like to read:\n")
    for data in file:
        if f.lower() in data.lower():
            print (data)
    file.close()
def ReadEntry():
    print("Your diary entries are 1")
    file = open(filename,"r")
    Entry = file.read()
    print (Entry)
    file.close()
    
    
def WriteEntry():
    Entry = input("What would you like to write?\n")
    file = open(filename,"a")
    d = GetDate()
    file.write ("\n"+ d) 
    file.write("\n"+ Entry)
    file.close()

while True:
    WelcomeMessage()
    print("Choose one of the following options  ")
    print("1. Read a previous entry")
    print("2. Write a new entry")
    print ("3. Search an entry") 
    print("9. Exit Journal")
    
    option = input("Enter your choice: ")
    print()
    if option == "1":
        ReadEntry()
        input("any key to continue:" )
    elif option =="2":
        WriteEntry()
        
    elif option == "3":
       SearchEntry()
       input ("enter to continue:") 
    elif option == "9":
        break 
    else:
        print("Invalid Option, Please enter 1/2/3")
