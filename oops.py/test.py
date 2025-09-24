class test:
    def m1(self):
        print("M1 method")
    @classmethod
    def m2(self):
        print("M2 method")
    @staticmethod
    def m3():
        print("M3 method") 
t1=test()
t1.m1()
t1.m2()
t1.m3()
t2=test()
t2.m1()
t2.m2()
t2.m3()
