def count_brackets(brackets):
    '''
    Takes a string of brackets like so: {{}} or }{{}}
    and tells us if it's balanced.
    '''
    count = 0

    for b in brackets:
        if b == "{":
            count = count + 1
        else:
            count = count - 1
        if count < 0:
            break
    
    return count == 0

if __name__ == "__main__":
    our_brackets = "}{{{{}"
    print(count_brackets(our_brackets))
