if __name__ == '__main__':
    # Here, I have a condition which strings together several
    # questions. You can chain these as much as you like in
    # Python!

    a_number = 10

    if (0 <= a_number <= 20) or (a_number != 9):
        print("The number is less than 20 but greater than 0!")
    else:
        print("Number is out of range!")