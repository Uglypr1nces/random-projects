search = input("What do you want to check")
searched = input("What do you want to search")


for letter in searched:
    if letter in search:
        print("found")

    else:
        print("not found")