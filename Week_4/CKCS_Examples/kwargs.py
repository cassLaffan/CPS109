
# Convention just says we name it kwargs
def print_a_family(**kwargs):
	for key, value in kwargs.items():
		print(key)
		print(*value)

if __name__ == "__main__":
	family_names = ["Cassandra", "Tavis", "Craig", "Susan"]
	fam_roles = ["Daughter", "Son", "Dad", "Mom"]

	print_a_family(roles = fam_roles, names = family_names)