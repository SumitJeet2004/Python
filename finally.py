def func1():
    try:
     l = [1,3,4,6,2]
     i = int(input("enter the index : "))
     print(l[i])
     return("success")
    

    except:
       print("error")
       return 0
    finally:
       print("finally")

x = func1()
print(x)


