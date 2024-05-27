# class Student:
#     school = "Akirachix"
#     def __init__(self,name,age,code):
#         self.name = name
#         self.age = age
#         self.code = code

class Student:
    school = "Akirachix"
    def __init__(self,first_name,last_name,age,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.code = code
    
    def greet_student(self):
        greeting = f"Hello {self.first_name}, welcome to {self.school}. your code is {self.code}"

        return greeting
    def year_of_birth(self):
        return f"{self.first_name} was born in {2024-self.age}"
    def student_full_name(self):
        return f"my name is {self.first_name} {self.last_name}"
    

# 23/05/2024

class Vehicle:
    def __init__(self,model,make):
        self.m