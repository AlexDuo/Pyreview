# Author: Real   
# CreateTime 5/31/2018-10:36 AM   
# IDE: PyCharm

class School(object):

    def __init__(self,schoolname,address):
        self.schoolname = schoolname
        self.address = address
        self.students=[]
        self.teachers=[]

    def enroll(self,student_obj):
        print('system has enrolled %s student'%student_obj.name)
        self.students.append(student_obj)



class SchoolMemeber:

    def __init__(self,name,age,sexual):
        self.name =name
        self.age = age
        self.sexual = sexual
        pass

    def tell(self):
        pass

class Teacher(SchoolMemeber):
    def __init__(self,name,age,sexual,salary,course):
        super(Teacher,self).__init__(name,age,sexual)
        self.salary = salary
        self.course = course


    def tell(self):
        print('''
        -----Teacher %s's information-----
        Name: %s
        Age: %s
        Sexual: %s
        Salary: %s
        Course: %s
        '''%(self.name,self.name,self.age,self.sexual,self.salary,self.course))


    def teaching(self):
        print('%s is teaching course [%s]'%(self.name,self.course))

class Student(SchoolMemeber):
    def __init__(self,name,age,sexual,student_id,grade):
        super(Student,self).__init__(name,age,sexual)
        self.student_id = student_id
        self.grade = grade

    def tell(self):
        print('''
        -----Student %s's information-----
        Name: %s
        Age: %s
        Sexual: %s
        Student_id: %s
        grade: %s
        '''%(self.name,self.name,self.age,self.sexual,self.student_id,self.grade))

    def pay_tuition(self,amount):
        print('%s student has paid %s tuition'%(self.name,amount))


s1 = School('Marquette University','2040 W Wisconsin Ave')

t1 = Teacher('Praveen',49,'M',15000,['Database system','Data Mining'])

stu1 = Student('Duo Zhang',27,'M','006045589','Graduate Student')


print(t1.course)

t1.tell()
s1.enroll(stu1)


