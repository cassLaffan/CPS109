age = 25
print("I am " + str(age) + " years old")

a = 13
b = 15
c = 13

print(a < b)
print(a < c)

print(a != b and b != c)

print(not (a == c))

print((a != c or b != c) and a == b)

if a > b or not (c == b) and (a > c or b > c):
	print("First condition!")
elif a == b:
	print("Second condition!")
elif c == b:
	print("Third condition!")
elif a != c:
	print("Fourth condition!")
else:
	print("Else condition!")


d = "HELLO"
e = "World"
f = "hello"

print(d == f)
print(d < f)