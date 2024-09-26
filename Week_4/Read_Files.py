'''
In this file, we will be using a function to read a file
and go through it line by line utilizing a for loop.

Notice that the file is treated as an iterable?
'''

def file_peak(): # Peaking at the file, getting content and lines
    num_lines = 0
    # Setting an empty string to add the contents from the file to
    file_contents = ""

    # You need to open the file temporarily with a while loop
    # There are other ways to open a file but this one ensures
    # your file closes after
    with open("a_file.txt") as f:
        # Iterable file object
        for line in f:
            file_contents = file_contents + line
            num_lines = num_lines + 1

    # Return a tuple containing the number of lines and file 
    # contents as a pair.
    return (num_lines, file_contents)

if __name__ == "__main__":
    t = file_peak()
    print(t[1])