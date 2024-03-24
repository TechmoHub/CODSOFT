import json
import textwrap
from task import Task
import os
import time

class Function:
    
    file_path = None
    data_list = []

    selected_task = None

    @staticmethod
    def run():
        while True:
            command = input("$ ").strip().lower().split(" ")
        
        
            match command[0]:

                case "addtask":
                    Function.addTask(command[1] if len(command) > 1 else None)

                case "select":
                    if len(Function.data_list) == 0:
                        print("The list is empty")

                    else:
                        os.system("cls")
                        Function.selected_task,data= Function.select_task(command[1] if len(command) >1 else None) 
                        Function.display(data)
                        print("Available commands: delete || track || update || goBack || editname || editdescription\n")

                case "goback":
                    Function.selected_task  = None
                    Function.refresh()

                case "save":
                    Function.update_database()
                
                case "editname":

                    Function.edit_name(command[1] if len(command) >1 else None)

                case "editdescription":

                    Function.edit_description()

                case "update":
                    Function.update_status(command[1] if len(command) > 1 else None)

                case "--help":
                    Function.display_commands()
                case "help":
                    Function.display_commands()

                case "refresh":
                    Function.refresh()

                case "clear":
                    os.system("cls")

                case "kill":
                    Function.file_path.close()
                    print("Saving the list...")

                    time.sleep(5)
                    print("List saved")
                    time.sleep(2)
                    break

                case "delete":
                    Function.delete_task(command[1] if len(command) >1 else None)

                case "track":
                     Function.track(Function.selected_task)
                    
                    
                case _:
                    print("Invalid command run 'help' to get a list of available commands")

    


    @staticmethod
    def update_database():
        
        
        _data = json.dumps(Function.data_list)
        Function.file_path.seek(0)
        Function.file_path.truncate()
        Function.file_path.write(_data)
        Function.refresh()
        

    @staticmethod
    def load_datbase():


        while True:
            try :
                Function.file_path = open("TO-DO LIST.json","r+")
            except FileNotFoundError as msg:
        
                Function.file_path = open("TO-DO LIST.json","w")
                Function.update_database()
                os.system("cls")
                Function.file_path.close()
            else:
                Function.data_list = json.load(Function.file_path)
                break

    @staticmethod
    def addTask(name = None):
        
        name = input("Enter the name of your task: ") if name ==None else name 
        task = Task(name)
       
        data = input("Enter the distription of your task(Optional): ")
        if data != "":
            task.data = data
        else:
            task.data = " "
    
        _data = task.dic()

        Function.data_list.append(_data)
        Function.update_database()
        


    @staticmethod
    def getList():

        if len(Function.data_list) == 0:
            return ["The list is empty"]
        else:
            return Function.data_list
        


    @staticmethod
    def display_commands():
        with open("--usage--.txt","r") as usage_file:
            usage = usage_file.readlines()
        for line in usage:
            print(line.replace('\n',''))   


    @staticmethod
    def frame(fun = None):
    
        def wrapper(*args):
            lenth = 140

            print("*"*lenth)

            if isinstance(fun(*args),tuple) :
                heading,names = fun(*args)

                print(f"*{' '*(70-(len(heading)//2) ) + heading + ' '*(68- ((len(heading)//2)+(len(heading)%2)))}*")

                if isinstance(names,list):

                    for name in names:
                        print(f"* {name +' '*(lenth-(3+len(name)))}*")
                else:

                    print(f"* {names +' '*(lenth-(3+len(names)))}*")
            elif isinstance(fun(*args),list) :
                heading,data = fun(*args)
                print(f"*{' '*62 + heading + ' '*63}*")    
                print(f"* {data+ " "*(lenth-(3+len(data)))}*")

                    
            print("*"*lenth)
        return wrapper



    @staticmethod
    @frame
    def display(LIST):

        
        if isinstance(LIST,dict):#Displays the selected task
            
            heading,names = Function.get_selected_task(LIST)
        
        elif len(LIST) != 0:
            heading,names = Function.get_list(LIST) 

        else:
                names = "List is empty."
                heading = "MY TO-DO LIST"

            
        
        return heading,names



    @staticmethod
    def select_task(task_num = None):
        task_num = input("Enter a task number: ") if task_num == None else task_num
        try:
            num = int(task_num)
            return (num,Function.data_list[num])#Returns task number and task dictionary
        except:
          return (None,[])

    @staticmethod
    def delete_task(task =None):
        
        task = Function.selected_task if task==None else task
        if task == None:
            print("No task selected")
        else:
            Function.data_list.pop(task)
            Function.update_database()
            Function.refresh()
        



    @staticmethod
    def refresh():
            os.system("cls")       
            Function.display(Function.data_list)


    @staticmethod
    @frame
    def track(task_num = None):

        task_num,task = Function.select_task(task_num) if task_num != None else [None,None]
 
        if task != None:
            status = "Complete" if task["done"] == True else "Not complete"
            return ["MY TO-DO LIST",task["name"]+ "  " + status]
        else:
            return ["MY TO-DO LIST","No task selected"]


    @staticmethod
    def get_selected_task(LIST):
            
            heading = LIST["name"]

            lines = textwrap.wrap(LIST["data"],135)
            data = lines+[" ",f"Status: {"Done" if LIST["done"] == True else "Not done"}"]
            
            return (heading,data)
    
    @staticmethod
    def get_list(LIST):
        heading = "MY TO-DO LIST"
        return (heading,[f"[{LIST.index(i)}] " +i["name"] for i in LIST])
    


    @staticmethod
    def update_status(status = None):

        if Function.selected_task == None:
            print("No task selected\n")
            return

        status = input("Enter 'True' to change the status to Complete otherwise 'False':\n") if status ==None else status

        Function.data_list[Function.selected_task]["done"] = bool(status)
        Function.update_database()



    @staticmethod
    def edit_name(name = None):
        
        if Function.selected_task == None:
            print("No task selected\n")
            return

        name = input("Enter the new name for your task:\n") if name ==None else name

        Function.data_list[Function.selected_task]["name"] = name
        Function.update_database()

    @staticmethod
    def edit_description():

        if Function.selected_task == None:
            print("No task selected\n")
            return

        override = input("Enter '0' to override the existing distription or '1' to add on the new line:\n")
        if override == '0' :
            description = input("Enter the new name for your task:\n")
        else: 
            description = Function.data_list[Function.selected_task]["data"]
            description = description + f"\n{input(f"{description}\n")}"
        Function.data_list[Function.selected_task]["data"] = description
        Function.update_database()

    