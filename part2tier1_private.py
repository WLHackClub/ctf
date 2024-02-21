flag = input('Enter flag: ')

# flag = 157 756 699 99

f1 = int(flag[:3])
f2 = int(flag[3:6])
f3 = int(flag[6:9])
f4 = int(flag[9:])

if f1 + f2 != 913:
    print('ACCESS DENIED')
elif f2 - f3 != 57:
    print('ACCESS DENIED')
elif f4 - f3 != -600:
    print('ACCESS DENIED')
elif f1 + f2 + f3 != 1612:
    print('ACCESS DENIED')
else:
    print('ACCESS GRANTED')
