'''B.Define a class person (attributes: name, department, date Of Birth). Derive two classes
employee (attributes: employee id, salary) and student (attributes: PRN, year, CGPA) from
person class. Derive two classes lab_assistant (attributes: labs) and faculty (attributes:
subject, number of research papers, qualification).

i) Create objects for lab assistant, faculties, and students.
ii) Display the data.
iii) Delete a data
iv) Find the total salary of all employees.
v) Find average CGPA of students department wise..'''
def see():
    print('''
    MENU
    i) Display the data.
    ii) Delete a data
    iii) Find the total salary of all employees.
    iv) Find average CGPA of students department wise
    v) exit
    ''')
class person:
    def __init__(self,name,department,birthdate):
        self.name=name
        self.department=department
        self.birthdate=birthdate

    def display(self):
        print("Name:",self.name)
        print("Department:", self.department)
        print("Date of birth:", self.birthdate)

class employee(person):
    def __init__(self,employeeid,salary,name,department,birthdate):
        self.employeeid=employeeid
        self.salary=salary
        person.__init__(self,name,department,birthdate)
    def display(self):
        print("Employee id:",self.employeeid)
        print("Salary:",self.salary)
        person.display(self)

class student(person):
    comp=0
    civil=0
    def __init__(self,prn,year,cgpa,name,department,birthdate):
        self.prn=prn
        self.year=year
        self.cgpa=cgpa
        person.__init__(self, name, department, birthdate)

        if department == 'Computer':
            student.comp += cgpa
        elif department == 'Civil':
            student.civil += cgpa
    def display(self):
        print("PRN:",self.prn)
        print("Year:",self.year)
        print("CGPA:",self.cgpa)
        person.display(self)

class lab_assistant(employee):
    lab_salary=0
    def __init__(self,lab,employeeid,salary,name,department,birthdate):
        self.lab=lab
        employee.__init__(self,employeeid,salary,name,department,birthdate)
        lab_assistant.lab_salary += salary

    def display(self):
        employee.display(self)
        print("lab:",self.lab)

class faculty(employee):
    faculty_salary=0
    def __init__(self,employeeid, salary, name, department, birthdate,subject, num_of_research_paper,qualification):
        self.subject=subject
        self.num_of_research_paper= num_of_research_paper
        self.qualification=qualification
        employee.__init__(self, employeeid, salary, name, department, birthdate)
        faculty.faculty_salary += salary
    def display(self):
        employee.display(self)
        print("Subject:",self.subject)
        print("Number of Research paper:", self.num_of_research_paper)
        print("Qualification:", self.qualification)

#Create objects for lab assistant, faculties, and students.
l1=lab_assistant('Python Lab',87,5000,'Ganesh','Computer','30/01/1995')
l2=lab_assistant('Mechanical Lab',96,5000,'Nilesh','Mechanical','05/07/1998')
l3=lab_assistant('Electrical Lab',87,5000,'Ramesh','Electrical','3/11/1993')

f1=faculty(177,20000,'Geeta','Computer','14/09/1990','Python',17,'M.tech')
f2=faculty(190,19000,'Seema','Mechanical','7/05/1994','Mechanics',14,'B.tech,M.tech')
f3=faculty(157,25000,'Avanti','Civil','25/12/1996','Hydrolis',27,'Ph.D')

s1=student(2030331245049,'2nd',9.47,'Rita Jadhav','Computer','21/03/2003')
s2=student(2130331245502,'2nd',9.02,'Pooja Patil','Civil','18/7/2001')
s3=student(2030331245078,'2nd',9.79,'Kajal Palkar ','Computer','3/03/2005')
s4=student(2030331245014,'2nd',9.83,'Rajesh Shinde','Civil','6/6/2006')

see()
while(True):
    key = int(input("Enter key:"))
    if key == 1:
        # Display the data.
        print("Lab Assistant Data:")
        l1.display()
        print()
        l2.display()
        print()
        l3.display()
        print()
        print("-------------------------------------------------------------------")

        print("Faculty Data:")
        f1.display()
        print()
        f2.display()
        print()
        f3.display()
        print()
        print("-------------------------------------------------------------------")

        print("Student Data:")
        s1.display()
        print()
        s2.display()
        print()
        s3.display()
        print()
        s4.display()
        print()
        print("-------------------------------------------------------------------")

    elif key == 2:
        print('''
         Enter key to delete data
         1)lab Assistant or Faculty
         2)Student
        ''')
        del_val=int(input("keys : "))
        if del_val == 1:
            k=int(input("Enter Employee ID:"))
            if l1.employeeid == k:
                print("Data of Lab Assistant {0} is Deleted!".format(l1.name))
                del l1
                print("remaining Lab Assistant Data:")
                l2.display()
                print()
                l3.display()
                print()
            elif l2.employeeid == k:
                print("Data of Lab Assistant {0} is Deleted!".format(l2.name))
                del l2
                print("remaining Lab Assistant Data:")
                l1.display()
                print()
                l3.display()
                print()
            elif l3.employeeid == k:
                print("Data of Lab Assistant {0} is Deleted!".format(l3.name))
                del l3
                print("remaining Lab Assistant Data:")
                l1.display()
                print()
                l2.display()
                print()

            elif f1.employeeid == k:
                print("Data of Faculty {0} is Deleted!".format(f1.name))
                del f1
                print("remaining Faculty Data:")
                f2.display()
                print()
                f3.display()
                print()

            elif f2.employeeid == k:
                print("Data of Faculty {0} is Deleted!".format(f2.name))
                del f2
                print("remaining Faculty Data:")
                f1.display()
                print()
                f3.display()
                print()

            elif f3.employeeid == k:
                print("Data of Faculty {0} is Deleted!".format(f3.name))
                del f3
                print("remaining Faculty Data:")
                f1.display()
                print()
                f2.display()
                print()
            else:
                print("Employee ID is not found!")
        if(del_val==2):
            k = int(input("Enter Student PRN no:"))
            if s1.prn == k:
                print("Data of Student {0} is Deleted!".format(s1.name))
                del s1
                print("remaining Student Data:")
                s2.display()
                print()
                s3.display()
                print()
                s4.display()
                print()

            elif s2.prn == k:
                print("Data of Student {0} is Deleted!".format(s2.name))
                del s2
                print("remaining Student Data:")
                s1.display()
                print()
                s3.display()
                print()
                s4.display()
                print()

            elif s3.prn == k:
                print("Data of Student {0} is Deleted!".format(s3.name))
                del s3
                print("remaining Student Data:")
                s1.display()
                print()
                s2.display()
                print()
                s4.display()
                print()

            elif s4.prn == k:
                print("Data of Student {0} is Deleted!".format(s4.name))
                del s4
                print("remaining Student Data:")
                s1.display()
                print()
                s2.display()
                print()
                s3.display()
                print()
            else:
                print("Student Data is not found!")
    elif key == 3:
        print("Total Salary of Lab Assistant:",lab_assistant.lab_salary)
        print("Total Salary of Faculty:",faculty.faculty_salary)
        total = lab_assistant.lab_salary + faculty.faculty_salary
        print("Total Salary of all Employees:",total)
        print()

    elif key == 4:
        comp_cgpa = student.comp/2
        civil_cgpa = student.civil/2
        print('Average CGPA of COMPUTER Department: ',comp_cgpa)
        print('Average CGPA of CIVIL Department: ',civil_cgpa)
        print()

    elif key == 5:
        exit()
    else:
        print("You Entered Wrong Data!!")







