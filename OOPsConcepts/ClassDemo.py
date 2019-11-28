class Employe:
    def __init__(self, Name, Idnumber, Location):
        self.name=Name
        self.id=Idnumber
        self.Address=Location
        print(id(self))

    def talk(self):
        print("Hello My name is:" + self.name)
        print("Hello My id is:" + self.id)
        print("Hello My Address is:" + self.Address)

s=Employe("Raghu","102","Hyderabad")
s.talk()
print(id(s))





