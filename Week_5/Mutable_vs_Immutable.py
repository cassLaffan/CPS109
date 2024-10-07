# This file simply shows what immutable vs. immutable means

if __name__ == "__main__":
    # You'll notice that you can do things like:
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_list.append(10)
    print(my_list)

    # But if you try it with a string, it will throw an error:
    my_string = "This is a string"
    # my_string.append("!")
    # Or a tuple...
    my_tuple = (1, 4, 7, 2, -11)
    #my_tuple.append(9)

    # This is all despite the fact that you can iterate through
    # both a string, a list and a tuple!
    for i in my_list:
        print(i)

    for j in my_string:
        print(j)

    for k in my_tuple:
        print(k)

    # Weird, right? That's because strings and tuples are immutable! You can't mess with them.
    # The only thing you can do is create new instances of tuples and strings with the 
    # assignment operator (=).
