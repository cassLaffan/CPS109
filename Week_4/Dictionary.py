'''
Here, we'll create a simple dictionary and use
some of the built in methods to manipulate it.
'''

if __name__ == "__main__":
    # Using curly braces
    person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # Using the dict constructor
    car = dict(make='Toyota', model='Camry', year=2022)

    # Accessing values
    print(person['name'])
    print(person['age'])

    # Let's update the person by giving her a new job.
    person['job'] = 'Engineer'

    # Now let's age her up
    person['age'] = 31  # Updates age to 31

    # Let's make her homeless and delete her city
    del person['city']  # Removes the city key-value pair

    # Or use pop to remove and return the value
    job = person.pop('job')  # Removes 'job' and returns its value


    # Let's check for a key...
    if 'name' in person:
        print("Name exists in the dictionary!")
    
    # Loop through the dictionary!
    for key in person:
        print(f"{key}: {person[key]}")

