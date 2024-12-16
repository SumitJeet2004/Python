with open ('sample.txt','w') as f:
    f.write("hello Jeet")
    f.truncate(10)
    
with open ('sample.txt','r') as f:
    print(f.read())