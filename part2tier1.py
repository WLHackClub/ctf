llllIIIlII = 913
lllIIIIlll = 57
llIIlIIIlI = 1570
lIIIllIIII = llllIIIlII + lllIIIIlll - llIIlIIIlI
IlIIllllIl = 1612
IlIIllIIlI = lllIIIIlll - 50
lllIIllIll = 4
IIllllIllI = input('Enter flag: ')
IIlllIllll = int(IIllllIllI[:lllIIllIll - 1])
IlIllIIIII = int(IIllllIllI[lllIIllIll - 1:6])
IIlIIlIlll = int(IIllllIllI[6:IlIIllIIlI + 2])
IIllIIIlII = int(IIllllIllI[IlIIllIIlI + 2:])
if IIlllIllll + IlIllIIIII != llllIIIlII:
    print('ACCESS DENIED')
elif IlIllIIIII - IIlIIlIlll != lllIIIIlll:
    print('ACCESS DENIED')
elif IIllIIIlII - IIlIIlIlll != lIIIllIIII:
    print('ACCESS DENIED')
elif IIlllIllll + IlIllIIIII + IIlIIlIlll != IlIIllllIl:
    print('ACCESS DENIED')
else:
    print('ACCESS GRANTED')
