class Operation:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __gt__(self, obj):
        a= self.x**3 + self.y**3
        b= obj.x**3 + obj.y**3
        return a>b
o1=Operation(2,3)
o2=Operation(4,1)
o1>o2