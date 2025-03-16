#initialize a class
class employee:
    #special method - constructer
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDH"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is now traveling to {destination}")

#creat a obj/instance of the class
sam = employee()

#print(sam.id)
#print(sam.salary)
#print(sam.designation)
#sam.travel("kerala")

print(type(sam))

from oops_proj import chatbook

user = chatbook()