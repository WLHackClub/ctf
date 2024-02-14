flag = int(input("Enter password: "))
c = bin(flag)
if len(c) != 10:
    print("ACCESS DENIED")
elif c[2] != "1":
    print("ACCESS DENIED")
elif c[3] != "0":
    print("ACCESS DENIED")
elif c[4:9] != "00000":
    print("ACCESS DENIED")
elif c[9] != "1":
    print("ACCESS DENIED")
else:
    print("ACCESS GRANTED")
