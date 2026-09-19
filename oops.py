class employee:
    def __init__(self):
        name = "Siddharth"
        age = 21
        designation = "data scientist"
        print(f'constructor initialized')
    
    def travel(self):
        print(f'Employee travelled to Russia')


emp = employee()

#print(emp.name)
emp.travel()