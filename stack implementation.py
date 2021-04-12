class Stack:
    def __init__(self,size):
        self.size=size
        self.data=[]
        self.top=-1
    def display(self):
        if self.top==-1:
            print("stack is empty")
            pass
        for i in range(self.top,-1,-1):
            print(self.data[i])
    def push(self,value):
        if self.top+1==self.size:
            print("stack overflow")
        else:
            self.top+=1
            self.data.append(value)
            
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            self.data.remove(self.data[-1])
            self.top-=1
s=Stack(4)
s.display()
s.push(30)
s.push(39)
s.push(37)
s.push(2)
s.push(22)
s.display()
s.pop()
s.pop()
s.display()
s.pop()
s.pop()
s.pop()
s.display()
