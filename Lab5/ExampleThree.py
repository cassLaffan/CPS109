# This file simply shows what immutable vs. immutable means

if __name__ == "__main__":
    # You'll notice that you can do things like:
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_list.append(10)
    print(my_list)

    # But if you try it with a string, it will throw an error:
    my_string = "This is a string"
    # my_string.append("!")

    # This is all despite the fact that you can iterate through
    # both a string and a list.
    for i in my_list:
        print(i)

    for j in my_string:
        print(j)

    # Weird, right? That's because strings are immutable! You can't mess with them.
    # The only thing you can do is create a new string.
