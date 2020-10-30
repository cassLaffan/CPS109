
def file_peak():
    num_lines = 0
    file_contents = ""

    with open("a_file.txt") as f:
        for line in f:
            file_contents = file_contents + line
            num_lines = num_lines + 1

    return (num_lines, file_contents)

if __name__ == "__main__":
    t = file_peak()
    print(t)