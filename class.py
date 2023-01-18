#class Employee :
#    def detail(self):
#        self.name = "EAI"
#        self.salary = 300
#        print("name = {}".format(self.name))
#        print("salary = {}".format(self.salary))

#emp1 = Employee()
#emp1.detail()

class Employee :
    def __init__(self) -> None:
        print("Default Constructor")
        
    def detail(self,name,salary):
        self.name = name
        self.salary = salary
        print("name = {}".format(self.name))
        print("salary = {}".format(self.salary))
        
obj1 = Employee()
obj1.detail("next",30000)

obj2 = Employee()
obj1.detail("wawa",50000)

