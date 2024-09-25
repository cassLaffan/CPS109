
def string_list():
    str_lst = []
    user_input = ""
    while user_input.lower() != "end":
        user_input = str(input("Please enter a movie to add to the list: "))
        if user_input.lower() != "end":
            str_lst.append(user_input)
    return str_lst

if __name__ == '__main__':
    local_list = string_list()
    lst_len = len(local_list)
    iterator = 0
    while iterator < lst_len:
        print("A movie is: ", local_list[iterator])
        iterator += 1