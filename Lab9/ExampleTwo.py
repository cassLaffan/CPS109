import random

def recurse_fruit(fruits, fruity_dict):
    
    if len(fruits) == 0:
        return
    elif len(fruits) == 1:
        fruity_dict[fruits[0]] = random.randint(0, 20)
    else:
        temp = int(len(fruits)/2) - 1
        recurse_fruit(fruits[:temp], fruity_dict)
        recurse_fruit(fruits[temp:], fruity_dict)
    
    return fruity_dict

if __name__ == "__main__":
    
    fruit_list = []
    for i in range(0, 5):  
        fruit_list.append(input("Please enter a fruit: "))
    
    fruit_dict = {}

    fruit_dict = recurse_fruit(fruit_list, fruit_dict)

    print(fruit_dict)