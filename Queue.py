class QUEUE:
    def __init__(self):
        self.QU=[]
        self.limit=0
        self.rp=-1
        self.fp=0
    def entry(self):
        self.limit=int(input("Enter for no. of terms: "))
        for i in range(self.limit):
            self.QU+=[None]
    def enque(self):
        if self.rp < self.limit-1:
            self.rp+=1
            self.QU[self.rp]=int(input("Enter term: "))
        else:
            print("OVERFLOW!!")
    def deque(self):
        if self.rp >= 0 and self.fp <= self.rp:
            print("Deque-ed: ",self.QU[self.fp])
            self.fp+=1
        else:
            print("UNDERFLOW!!")
    def peek(self):
        if self.rp >= 0 and self.fp <= self.rp:
            print(self.QU[self.fp])
        else:
            print("EMPTY!!")
    def display(self):
        if self.rp >=0 and self.fp <= self.rp:
            for i in range(self.fp,self.rp+1):
                print(self.QU[i],end=' ')
        else:
            print("EMPTY!!")
#main-------------------------------------------------------------------------
def main():
    Ob=QUEUE()
    Ob.entry()
    print("1) Enque")
    print("2) Deque")
    print("3) Peek")
    print("4) Display")
    print("5) Exit")
    while(True):
        ch=int(input("\nEnter your choice(1-5): "))
        if ch == 1:
            Ob.enque()
        elif ch == 2:
            Ob.deque()
        elif ch == 3:
            Ob.peek()
        elif ch == 4:
            Ob.display()
        elif ch == 5:
            import sys
            sys.exit()
        else:
            print("INVALID INPUT!!")
            print("Try again....")
main()        

