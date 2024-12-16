#f = open('myfile2.txt' , 'w')

#text = f.read()
#print(text)
#f.close()

f = open('myfile2.txt' , 'w')
f.write('Hello World\n')
f.close()

with open('myfile2.txt','a') as f:
    f.write("hey i'm inside with ")