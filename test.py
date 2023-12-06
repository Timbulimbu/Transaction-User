class Person():
    def __init__(self, name, fname, age):
        self.name = name
        self.fname = fname
        self.age = age

person1 = Person('Иван', 'Иванов', 25)
person2 = Person('Петр', 'Петров', 30)
person3 = Person('Сидор', 'Сидоров', 35)


for attr in dir(person1):
    if not callable(getattr(person1, attr)) and not attr.startswith('__'):
        print(attr, ":",  getattr(person1, attr))
        
for attr in dir(person2):
    if not callable(getattr(person2, attr)) and not attr.startswith('__'):
        print(attr, ":",  getattr(person2, attr))
        
for attr in dir(person3):
    if not callable(getattr(person3, attr)) and not attr.startswith('__'):
        print(attr, ":",  getattr(person3, attr))




