i = 4
while True:
    if i == 0:
        if flag == "3851":
            print("ACCESS GRANTED")
    elif i == 1:
        if a != b:
            print("ACCESS DENIED")
            break
        i = 9
    elif i == 2:
        a = int(flag) % 100
        b = int(flag) // 100
        i = 6
    elif i == 3:
        if a % 10 != 4:
            print("ACCESS DENIED")
            break
        i = 8
    elif i == 4:
        flag = input("Enter password: ")
        i = 2
    elif i == 5:
        if flag == "1447":
            print("ACCESS GRANTED")
    elif i == 6:
        if b > 100:
            print("ACCESS DENIED")
            break
        i = 1
    elif i == 7:
        if a < 10:
            print("ACCESS DENIED")
            break
        i = 3
    elif i == 8:
        print("ACCESS GRANTED")
        break
    elif i == 9:
        if a > 20:
            print("ACCESS DENIED")
            break
        i = 7
