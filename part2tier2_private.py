flag = input('Enter password: ')

# flag = BetterTodayThenYesterday

if flag[:6] != 'Better':
    print('ACCESS DENIED')
elif flag[6:11] != 'Today':
    print('ACCESS DENIED')
elif flag[11:15] != 'Then':
    print('ACCESS DENIED')
elif flag[15:] != 'Yesterday':
    print('ACCESS DENIED')
else:
    print('ACCESS GRANTED')
