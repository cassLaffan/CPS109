new_list = []

print(new_list)

# Produces index error!
# print(new_list[1])

new_list.append("This is an element\n")
new_list.extend(["apple", "banana", "grape\n"])
new_list.append(10)

print(new_list)
print(new_list[0], new_list[3])