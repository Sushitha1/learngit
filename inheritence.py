class Driver:
    def __init__(self,id,name,email,wallet):
        self.id = id
        self.name= name
        self.email= email
        self.wallet= wallet
    def userinfo(self):
        print(f"{self.id},{self.name},{self.email},{self.wallet}")
d1= Driver(10,"Sanju","sanju@gmail.com",867)
d1.userinfo()
class Customer(Driver):
    def __init__(self,id,name,email,wallet,offer):
        super().__init__(id,name,email,wallet)
        self.offer=offer
    def discount(self):
        if self.offer is True:
            d=int(input("Give discount %: "))
            a= int(self.wallet) - (int(self.wallet)*(d/100))
        else:
            print("No discount")
        print(a)
a=0           
c1=Customer(1,"Sahruday","sah@gmail.com",4857,True)
c1.userinfo()
c1.discount()