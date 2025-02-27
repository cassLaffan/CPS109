if __name__ == "__main__":
    a_list = [1, 2, "three"]
    a_list.append([4, 5])
    print(a_list)
    a_list.pop()
    print(a_list)
    a_list.extend([4, 5])
    print(a_list)

    for i in range(len(a_list)):
        if i == 2:
            continue
        print(a_list[i])
