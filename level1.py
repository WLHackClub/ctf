f = input("Enter password: ")
a = int(f[0])
b = int(f[1])
c = int(f[2])
d = int(f[3])
if b != c:
    print('ACCESS DENIED')
elif c != d:
    print('ACCESS DENIED')
elif a != b - 2:
    print('ACCESS DENIED')
elif a + b + c == 25:
    print('ACCESS GRANTED')
else:
    print('ACCESS DENIED')
