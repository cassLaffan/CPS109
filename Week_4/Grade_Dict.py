if __name__ == "__main__":
    # Creating a dictionary
    grade_dict = {"John" : [99, 86, 90, 80],
                  "David" : [100, 75, 80, 82],
                  "Harsimran" : [60, 99, 79, 100],
                  "Jatin" : [98, 99, 100, 80]
                  }

    # Adding new key-value pairs to the dictionary
    grade_dict["Yanis"] = [80, 81, 79, 90]
    grade_dict["Moaed"] = [85, 85, 85, 85]

    # Changing a value in an existing key-value pair
    grade_dict["David"].append(90)

    for key in grade_dict:
        print(key, "'s grades are: ", grade_dict[key])
