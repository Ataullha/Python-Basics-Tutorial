class Employee:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
    
    def display(self):
        print('id:',self.id,'\n'+'name:',self.name)

emp = Employee(2018331081,'Md Ataullha')

emp.display()

del emp.id

try:
    print(emp.id)
except Exception as e:
    print(e)

del emp

try:
    print(emp)
except Exception as e:
    print(e)