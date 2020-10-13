def int_func():
    char = 0
    for i in input("Enter words with a space(lower latin script):\n").split():
        for score, letter in enumerate(i):
            if 97 <= ord(letter) <= 122:
                char += 1
        if char == len(i):
            print(i.title())
        else:
            print("Only small English letters!")


int_func()