option = "0"
numbers_list = []

def menu():
    print("MENU")
    print("-------------------------------------------")
    print("1. Add a number to the list")
    print("2. Add a number in a position in the list")
    print("3. Show the length of the list")
    print("4. Delete the last number in the list")
    print("5. Delete a number in the list")
    print("6. Count numbers")
    print("7. Positions of a numbers")
    print("8. Show the list")
    print("9. Exit")
    
def add_number_to_list(number):
    numbers_list.append(number)
    

def add_number_to_x_position(number, position):
    if int(position) <= len(numbers_list):
        numbers_list.insert(int(position), number)
    return False
    
def show_lenght_of_list():
    return len(numbers_list)

def delete_last_number():
    last_number = numbers_list.pop()
    return last_number

def delete_number_from_position(position):
    if position <= len(numbers_list):
        deleted_number = numbers_list.pop(position)
        return deleted_number
    return False

def count_numbers(number):
    times = numbers_list.count(number)
    return times
    
def position_of_number(number):
        position = 0
        indexes = []
        
        for element in range(0, numbers_list.count(number)):
            index = numbers_list.index(number, position)
            indexes.append(index)
            position = index + 1
        
        return show_list(indexes)
    
def show_list(numbers_list):
        for elements in numbers_list:
            print(elements, end=" ")
        print()

while True:
    
    menu()

    option = input("What would you like to do?")

    if option == "1":
        number = input("What number would you like to add?")
        add_number_to_list(number)
    
    elif option == "2":
        number = input("What number would you like to add?")
        position = input("In which position?")
        add_number_to_x_position(number, position)

    elif option == "3":   
        print("List has this length:",show_lenght_of_list())

    elif option == "4":
        print("Deleted",delete_last_number())

    elif option == "5":
        position = int(input("In which position?"))      
        print("Deleted number",delete_number_from_position(position))

    elif option == "6":
        number = input("What number would you like to count?")
        print("The number appears",count_numbers(number),"times.")

    elif option == "7":
        number = input("What number would you like to search in the list?")
        position_of_number(number)

    elif option == "8":
        show_list(numbers_list)
    
    elif option == "9":
        break