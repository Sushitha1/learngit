class Employee:
    def __init__(self,e_id,fullname,email,salary,interest):
        self.e_id= e_id
        self.fullname= fullname
        self.email= email
        self.salary= salary
        self.interest= interest
    def details(self):
        print("Employee id of 1st employee:",self.e_id)
        print("First name of 1st employee:",((self.fullname).split())[0])
        print("Last name of 1st employee:",((self.fullname).split())[1])
    
o1=Employee(1,"SUSHITHA MACHA","machasushitha@gmail.com",50000,"dancing")
o2=Employee(2,"Vruddi Shah","vruddishah@gmail.com",70000,"Singing")
o1.details()
o2.details()





