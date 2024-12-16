a = input("enter ther number")
print(f"multiplication table of {a} is : ")

try:

 for i in range(1,21):
    print(f"{int(a) } * {i} = {int(a)*i}")
except Exception as e:
   print(e)
  

