'''
Here's a file where we take some of the functions used
to manipulate strings and actually use them!
'''

if __name__ == "__main__":
    # Take user input
    user_input = input("Please enter a sentence: ")

    # Makes a new string, all lowercase
    upper_case = user_input.upper()
    print("Uppercase:", upper_case)

    # Makes a new string, all lowercase
    lower_case = user_input.lower()
    print("Lowercase:", lower_case)

    # Creates a new string, whitespace removed
    stripped_input = user_input.strip()
    print("Stripped input (whitespace removed):", stripped_input)

    # Splits the string based on a specifier (blank is default)
    split_words = user_input.split()
    print("Split words:", split_words)

    # Joins strings
    joined_string = " - ".join(split_words)
    print("Joined string with ' - ':", joined_string)

    # Replaces one character with another in a string
    replaced_string = user_input.replace(" ", "_")
    print("String with spaces replaced by underscores:", replaced_string)
