# Additional Mutability Example

if __name__ == "__main__":

	teenage_mutable_ninja_turtles = ["Raphael", "Donatello", "Leonardo", "Michelangelo"] # Remember, lists are mutable - strings are not
	teenage_mutable_ninja_turtles.append("Splinter") # We can add new elements
	teenage_mutable_ninja_turtles.pop() # We can also remove elements (Shoo Splinter, you aren't a turtle!)

	for immutable_turtle in teenage_mutable_ninja_turtles:
		immutable_turtle = "B" + immutable_turtle[1:]
	print(teenage_mutable_ninja_turtles) # Notice how it doesn't change. This is due to how for loops work (we're modifying the 
										 # immutable_turtle variable, which is local to the for loop).

	for i in range(len(teenage_mutable_ninja_turtles)):
		teenage_mutable_ninja_turtles[i] = "B" + teenage_mutable_ninja_turtles[i][1:]
	print(teenage_mutable_ninja_turtles) # Notice how it does change, but we need an equals sign to do so (we are making a new string)

	#teenage_mutable_ninja_turtles[0][0] = "R" # We can't change strings like this!
	teenage_mutable_ninja_turtles[0] = "Baphael!" # But we can change list items to whole new strings

	teenage_mutable_ninja_turtles[0].replace("B", "R", 1)
	print(teenage_mutable_ninja_turtles[0]) # Notice how it doesn't change
	teenage_mutable_ninja_turtles[0] = teenage_mutable_ninja_turtles[0].replace("B", "R", 1)
	print(teenage_mutable_ninja_turtles[0]) # Notice how it does change, but we are setting it to the new string returned by the .replace() method