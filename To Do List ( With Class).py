class ToDoList:
    def __init__(self):
        self.task=[]
        self.menu=["Add Task", "Remove Task", "Show Task", "Sort Task", "Save Task", "Load Task"] 
        self.select=[self.addTask,self.removeTask,self.showTask,self.sortTask, self.saveTask, self.loadTask]
        self.filename = "ToDoList.txt"
    
    def addTask(self):
        print("Adding Task")
        print (" Write the task you would like to add below:")
        Tasks = input("Add Task: ")
        self.task.append(Tasks) 
        
        
    def removeTask(self):
        print (" Removing Task")
        
    def showTask(self):
        print("Showing Task")
        print (self.task)
    
    def sortTask(self):
        print("Sorting Task")
        self.task.sort()
        print (self.task) 
        
    def saveTask(self):
        print ("Saving Task")
        f = open(self.filename,"w")
        for item in self.task:
            f.write(item)
            f.write("\n")
              
    def loadTask(self):
        print("Loading Task")
        
    def displayMenu(self):
        print("Showing Menu")
        print ("Choose one of the following:\n")
        for i in range(len(self.menu)):
            print(f"{i}. {self.menu[i]}")
        self.chooseTask()  
   
    def chooseTask(self):
        while True:   
            print (f" Enter number 0-{len(self.menu)-1} and 9 to quit")
            x = int(input())
            if x ==9:
                print (" Thank you for using ToDoList Program")
                print ("Have a nice day") 
                break
            self.select[x]()
        

toDoList = ToDoList()
toDoList.displayMenu() 
        
        
                
    
