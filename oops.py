class employee:
    def __init__(self):
        self.name = "Siddharth"
        self.age = 21
        self.designation = "data scientist"
        print(f'constructor initialized')
    
    def travel(self):
        print(f'Employee travelled to Russia')


emp = employee()

#print(emp.name)
emp.travel()