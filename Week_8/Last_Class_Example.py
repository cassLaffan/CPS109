# Function to prompt the user for key-value pairs
def get_entries(entries):
    while True:
        key = input("Enter the key (or 'done' to stop): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter the value for key '{key}': ")
        entries.append((key, value))

# Function to sort the list by the second element of each tuple
def sort_entries(user_entries):
    sorted_entries = sorted(user_entries, key=lambda x: x[1])  # Sort by the second element (value)
    return sorted_entries

if __name__ == "__main__":
    entries = []
    # Main program flow
    get_entries(entries)
    sort_entries(entries)

    # Display the sorted list
    print("\nSorted entries (by value):")
    for entry in sort_entries:
        print(entry)