x = int(input("enter the number"))
match x :
    case 1: print('one')
    case 2: print('two')
    case _ if x!=10:
        print('other than ten')
    case _: print(x)