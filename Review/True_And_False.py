if __name__ == "__main__":
    var = 8 < 10 and 9 == 9
    print(var)

    var_b = 7 != 7 or 7 != 6
    print(var_b)
    print(not var_b)
    var_int = 7
    str_int = "Hello"
    print(f"{str_int} is {var_int}")
    print(str(var_int) + str_int)
