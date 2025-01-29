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
    # Enumerate allows us to get an index-value pair from a list or tuple
    for iterator, movie in enumerate(local_list):
        print(f"Movie number {iterator + 1} is {movie}") # Another f string!