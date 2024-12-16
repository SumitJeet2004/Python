with open('file.txt', 'r') as f:
    print("Type of file object:", type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print("Data read from file:", data)
