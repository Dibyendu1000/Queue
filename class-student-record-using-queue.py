print('Student Record using Queue')
#=====================================================
class Student():
    def __init__(self,n,r,c):
        self.name=n
        self.clas=c
        self.roll=r
#================================================
    def __str__(self):
        string="Student's Name:"+str(self.name)+"\nRoll No.:"+\
                str(self.roll)+"\nClass:"+str(self.clas)
        return string
#======================================
class Queue:
    def __init__(self):
        self.List=[]
        self.rp=-1
        self.fp=0
        self.n=0
#===========================================================================
    def Entry(self):
        self.List=[]
        self.rp=-1
        self.fp=0
        self.n=int(input('Enter no.of records:'))
        for i in range(self.n):
            self.List.append(None)
#===========================================================================
    def Insert(self):
        if self.rp>=self.n-1:
            print('-'*10)
            print('Queue is Full')
            print('-'*10)
        else:
            n=input("Enter Students' Name:")
            c=input('Enter class:')
            r=int(input('Enter roll no.:'))
            Stud=Student(n,r,c)
            self.rp+=1
            self.List[self.rp]=Stud
#===========================================================================
    def Delete(self):
        if self.fp>self.rp:
            self.fp=0
            self.rp=-1
            print('Queue is Empty')
        else:
            print('-'*10)
            print('Deleted:',self.List[self.fp])
            self.fp+=1
            print('-'*10)
#===========================================================================            
    def Display(self):
        if self.fp>self.rp:
            self.rp=-1
            self.fp=0
            print('-'*10)
            print('Queue is Empty')
            print('-'*10)
        else:
            print('-'*10)
            print('Displaying the Queue')
            for i in range(self.fp,self.rp+1,+1):
                print(self.List[i],end=' ')
            print('-'*10)
#============================================================================
    def Choose(self):
        while True:
            print('\n1.Entry')
            print('2.Insert')
            print('3.Delete')
            print('4.Display')
            print('5.Exit')
            ch=int(input('Enter your choice:'))
            if ch==1:
                self.Entry()
            elif ch==2:
                self.Insert()
            elif ch==3:
                self.Delete()
            elif ch==4:
                self.Display()
            else:
                break
#=============================MAIN============================================
ob=Queue()
ob.Choose()
                
            
            
