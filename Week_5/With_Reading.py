'''
Here, we will examine using the "with" keyword
again while reading a file!
'''

if __name__ == "__main__":
    with open('Spooky.txt', 'r') as file:
        # Reads everything
        content = file.read()
        print(content)

    with open('halloween.txt', 'r') as file:
        # Reads the first line
        first_line = file.readline()
        # Reads all the lines   
        all_lines = file.readlines()
        print("First line:", first_line)
        print("All lines:", all_lines)
