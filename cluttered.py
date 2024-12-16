import os

files = os.listdir("fileimg")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"fileimg/{file}",f"fileimg/{i}.png")
        i+=1
        print(file)