# 1. 
def displayNamespace():
    """ Write a Python program to import built-in array module and display the namespace of the said module. """
    import string
    for each in string.__dict__:
        print(each, end="")
# displayNamespace()

# 2.
class Display:
    """ Write a Python program to create a class and display the namespace of the said class. """
    def namespace(self):
        for each in Display.__dict__:
            print(each)
# instance = Display()
# instance.namespace()

# 3.
class Namespace:
    """ Write a Python program to create an instance of a specified class and display the namespace of the said instance. """
    def __init__(self, namespace):
        self.namespace = namespace

instance = Namespace('nothing but space')
for each in instance.__dict__:
    pass
    # print(each)

# 4.
def builtinsFunc():
    """ 'builtins' module provides direct access to all 'built-in' identifiers of Python.
    Write a python program which import the abs() function using the builtins module, 
    display the documentation of abs() function and find the absolute value of -155
    """
    import builtins
    help(builtins.abs)
    print(builtins.abs(-155))
# builtinsFunc()

# 5.
def student(**kwargs):
    """ Define a Python function student(). Using function attributes display the names of all arguments. """
    print(f'''
        Student Name: {kwargs["name"]}
        Student Age: {kwargs["age"]}
        Student Job: {kwargs["job"]}
        Marital Status: {kwargs["marital_status"]}
    ''')
# student(name='kennedy', age=31, job='Software Developer', marital_status='Single')

# 6.
class Student:
    """ Write a simple Python class named Student and display its type. 
    Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
    """
    _private = "I am private."
    __more_private = "I am more private."
    def __str__(self):
        return f"""
        {type(Student())}
        {Student.__dict__.keys()}
        {Student.__module__}
        """
# me = Student()
# print(me)

# 7.
class Student2:
    """
    Write a Python program to crate two empty classes, Student and Marks. 
    Now create some instances and check whether they are instances of the said classes or not. 
    Also, check whether the said classes are subclasses of the built-in object class or not.
    """
    pass
class Mark:
    pass

student1 = Student2()
mark = Mark()
def main01():
    print(isinstance(student1, Student2))
    print(isinstance(mark, Student2))
    print(issubclass(Student, object))
    print(issubclass(Mark, object))

# 8.
class Student3:
    student_id = 'stud-01'
    student_name = 'Kennedy'

me = Student3()

# ONE WAY
def student3Main0():
    print(f"Original: {me.student_id, me.student_name}")
    me.student_id = 'stud-02'
    me.student_name = 'anothername'
    print(f"Modified: {me.student_id, me.student_name}")

# ANOTHER WAY
def student3Main1():
    print(f"Student Name: {getattr(Student3, 'student_name')}")
    print(f"Student ID: {getattr(Student3, 'student_id')}")
    setattr(Student3, "student_name", "Samrawit")
    setattr(Student3, "student_id", 'stud-02')
    print(f"Student Name: {getattr(Student3, 'student_name')}")
    print(f"Student ID: {getattr(Student3, 'student_id')}")

# 9.
class Student4:
    """
    Write a Python class named Student with two attributes student_id, student_name. 
    Add a new attribute student_class and display the entire attribute and their values of the said class. 
    Now remove the student_name attribute and display the entire attribute with values.
    """
    student_name = "Kennedy"
    student_id = "KEn254"

def student4Main2():
    setattr(Student4, 'student_class', 'Python')
    print(f"Student Name: {getattr(Student4, 'student_name')}")
    print(f"Student ID: {getattr(Student4, 'student_id')}")
    print(f"Student Class: {getattr(Student4, 'student_class') if isinstance('student_class', Student4) else print('Does not exist')}")
student4Main2()

# 10.
