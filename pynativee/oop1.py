class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks
    def average(self):
         sum = 0
         for value in self.marks:
             sum += value
         print(self.name,sum/3)
s1 = Student("shovon",[45,43,47])
s1.average()     
  


