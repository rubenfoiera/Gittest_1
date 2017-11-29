from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,module):
        self.modules.append(module)
        self.grades[module] = Module.get_grade  # The grade is accessed from get_grade from Module.

    def get_list_modules(self):
        for item in self.modules:
            print(item)

    def get_grades(self):
        for item in self.grades:
            print(item)


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
