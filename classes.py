
'''class Employee:
    Common base class for all employees
    empCount = 0 # class variable shared by all instances
    def __init__(self, name, salary): #constructor
        self.name = name #instance variable unique to each instance
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
p=Employee('ojas',1400)
p.displayCount()
p.displayEmployee()
print(p.name)'''
class Employee:
    empCount = 0
    def __init__(self, empid, empname, empsal, empdept):
        self.name = empname
        self.sal = empsal
        self.id = empid
        self.dept = empdept
    def details(self):
        print("Name : ", self.name, ", Salary: ", self.sal,",ID:",self.id,",dept:",self.dept)
class timesheet(Employee):
    def __init__(self,date,hrs,activity,description,status):
        self.date =date
        self.hrs =hrs
        self.act =activity
        self.desc =description
        self.sts=status
    def table(self):
        print( "date:", self.date,"  hrs:",self.hrs,"  activity:", self.act, "  desc:",self.desc, "  sts:",self.sts)
p=Employee(20853,'ojas',1400,'JOB')
p.details()
p=timesheet('29.09.2021', 8,'none','job','done')
p.table()