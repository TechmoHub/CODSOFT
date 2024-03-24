import secrets
import string
import os

os.system("cls")



def main():

    while True:
        
        length = validate_length() 
        if length == -1:
            os.system("cls")
            break 
        complexity = validate_complexity()
  
        password = generate_password(length,complexity)
        print("\nYour password is:",password)
        print("\nEnter -1 to stop the program")

def generate_password(length,complexity):

    characters = [
        string.ascii_letters, #complexity level 1
        string.ascii_letters + string.digits, #complexity level 2
        string.ascii_letters + string.digits + string.printable,#complexity level 3
    ]

    complexity_level = complexity-1
    characters_set = characters[complexity_level]

    password = "".join(secrets.choice(characters_set) for _ in range(length))

    return password


def validate_length():
    while True:
        length = int(input("Enter the length(it should be more than 4) of the password: "))
        if length >=5:
            return length
        elif length == -1:
            return -1
        
def validate_complexity():
    while True:
        complexity = int(input("Choose the level of complexity in the range of 1 to 3: "))
        if 1<= complexity <=3:
            return complexity

if __name__ == "__main__":
    main()