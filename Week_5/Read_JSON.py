import json
'''
In order to use json functionality, we need to import
the json library.
'''

if __name__ == "__main__":
    # Load the spooky data from the JSON file
    with open('Spooky.json', 'r') as file:
        spooky_locations = json.load(file)

    # Display the haunted locations
    for location in spooky_locations['haunted_locations']:
        if location['haunting']:
            print(f"Beware! {location['name']} in {location['location']} has {location['ghosts']} ghosts haunting it!")
        else:
            print(f"{location['name']} in {location['location']} seems safe... for now.")
