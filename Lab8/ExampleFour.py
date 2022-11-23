# This file shows you how to make a dictionary
# and then look things up in it given a key value.

if __name__ == "__main__":
    # This is how you declare an empty dictionary
    # Dictionaries are mutable, much like lists, so you can
    # add stuff to it as need be.
    name_dict = {}

    inp = "-1"
    emp_num = ""

    while inp != "":
        inp = str(input("Please enter an employee name. To exit, press 'enter' with no name.\n"))
        if inp == "":
            break
        else:
            emp_num = str(input("Now please enter their employee number.\n"))
            while emp_num == "":
                emp_num = str(input("Bad input! Please input an employee number.\n"))

            # This is the syntax for adding a new key-value pair to an existing dictionary
            # dictionary[key] = value
            if inp in name_dict:
                temp = name_dict[inp]
                name_dict[inp] = []
                name_dict[inp].append(temp)
                name_dict[inp].append(emp_num)
            else:
                name_dict[inp] = emp_num
    
    print(name_dict)

    print("Goodbye")