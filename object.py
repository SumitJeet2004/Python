class person:
    name="sumit"
    age=25
    occupation="enginieer"
    networth = 100
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()
a.name = "jeet"
a.occupation="doctor"
b.name="anu"
b.occupation="house wife"

a.info()
b.info()
c.info()

