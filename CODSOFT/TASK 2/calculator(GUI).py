import os

os.system("cls")


def main():



    num_1 = input("Enter the first number: ").strip()
    while not (validate_num(num_1)):
        num_1 = input("Please enter valid number: ").strip()


    operation = input("Enter one of the following operations '+,-,*,/': ").strip()
    while not(validate_operation(operation)):
        operation = input("Please enter one of the following operations ' + , - , * , / ': ").strip()


    num_2 = input("Enter the second number: ").strip()
    while not (validate_num(num_2)):
        num_2 = input("Please enter valid number: ").strip()


    os.system("cls")
    print(f"The answer to: {num_1 + operation + num_2} = {eval(num_1+operation+num_2)}")

def validate_num(num):

    try:
        num = int(num)
    except:
        return False

    else:
        return True
    

def validate_operation(oporator):

    if oporator in ['+','-','*','/']:
        return True
    else:
        return False


if __name__ == "__main__":

    main()