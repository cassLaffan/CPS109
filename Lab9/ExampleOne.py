import random

def recurse_dict(name_list, re_dict):
    
    if len(name_list) == 1:
        re_dict[name_list[0]] = random.randint(1, 100)
        return recurse_dict
    else:
        re_dict[name_list[0]] = random.randint(1, 100)
        recurse_dict(name_list[1:], re_dict)

    return re_dict

if __name__ == "__main__":
    user_list = []
    for i in range(1, 10):
        user_list.append(input("Please enter a name: "))

    new_dict = {}

    new_dict = recurse_dict(user_list, new_dict)

    print(new_dict)