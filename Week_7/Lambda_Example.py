'''
Here is an example of a lambda, which is an in-line, short, anonymous
function.
'''
if __name__ == "__main__":
    sum_of_squares = lambda x, y: x*x + y*y
    print(sum_of_squares(3, 8)) 

    data = [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 25},
            {'name': 'Jesse', 'age': 18}]
    '''
    ret = lambda x, y: x[y]['age']
    for item in range(len(data)):
        print(ret(data, item))
    '''
    sorted_data = sorted(data, key=lambda x: x['age'])  # Sort by age
    print(sorted_data)