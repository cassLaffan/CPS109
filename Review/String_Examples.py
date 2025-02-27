if __name__ == "__main__":
    string_a = "Hello!"
    string_b = "World!"

    string_a = string_a  + string_b
    string_b = string_b.upper()

    print(string_a)
    print(string_b)

    new_string = "      My mom told me to get \"apples\" please?"
    stripped_string = new_string.strip()
    print(stripped_string)
    split_string = new_string.split()
    print(split_string)
    joined_string = "_".join(split_string)
    print(joined_string)
