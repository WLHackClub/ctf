flag = input('Enter password: ')

# flag = BetterTodayThenYesterday

if flag[:6] != 'Better':
    print('ACCESS DENIED')
elif flag[6:11] != 'Today':
    print('ACCESS DENIED')
elif flag[11:15] != 'Then':
    print('ACCESS DENIED')
elif flag[15:24] != 'Yesterday':
    print('ACCESS DENIED')
else:
    # flag = 157 756 699 99
    f1 = int(flag[24:27])
    f2 = int(flag[27:30])
    f3 = int(flag[30:33])
    f4 = int(flag[33:35])
    if f1 + f2 != 913:
        print('ACCESS DENIED')
    elif f2 - f3 != 57:
        print('ACCESS DENIED')
    elif f4 - f3 != -600:
        print('ACCESS DENIED')
    elif f1 + f2 + f3 != 1612:
        print('ACCESS DENIED')
    else:
        if flag[35:] == 'the missile knows...':
            print('ACCESS GRANTED')
        else:
            print('ACCESS DENIED')
