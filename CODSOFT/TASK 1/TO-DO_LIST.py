
import os
from functions import Function
 
os.system("cls")

def main():
    
    Function.load_datbase()
    Function.display(Function.data_list)
    Function.display_commands()

    Function.run()
    os.system("cls")




if __name__ == "__main__":
    main()