my_dict = dict()

my_dict["Banana"] = "Yellow"
my_dict["Apple"] = ["Red"]
my_dict["Strawberry"] = "Red"
my_dict["Grape"] = "Purple"
my_dict["Guava"] = "Green"

my_dict["Apple"].append("Green")

print(my_dict)

del my_dict["Guava"]

print(my_dict)

bana_colour = my_dict.pop("Banana")

print(bana_colour)

print(my_dict)

for key in my_dict:
	print(key)
	print(my_dict[key])