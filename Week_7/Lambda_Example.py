'''
Here is an example of a lambda, which is an in-line, short, anonymous
function.
'''
if __name__ == "__main__":
    sum_of_squares = lambda x, y: x*x + y*y
    print(sum_of_squares(3, 4)) 

    data = [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 25}]
    sorted_data = sorted(data, key=lambda x: x['age'])  # Sort by age
    print(sorted_data)