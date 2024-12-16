class person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name = n
        self.occ= o
    def info(self):
        print(f"my name is {self.name} and i am a {self.occ}")

a=person("jeet","dr")
b=person("anu","HR")

a.info()
b.info()  # here we are creating two objects a and b and calling the method info()

        