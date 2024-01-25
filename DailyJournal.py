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
    x = input("Enter the date of the entry you would like to read, (DDMMYY): ")
    file = 
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
    print("3. Exit Journal")
    
    option = input("Enter your choice: ")
    print()
    if option == "1":
        ReadEntry()
        break 
    elif option =="2":
        WriteEntry()
        break
    elif option == "3":
        break
    else:
        print("Invalid Option, Please enter 1/2/3")


    
        
        
    

    
    

    
