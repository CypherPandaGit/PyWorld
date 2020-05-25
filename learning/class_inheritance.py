class A:

    def feature1(self):
        print('Feature 1 working.')

    def feature2(self):
        print('Feature 2 working too.')


#class B():
class B(A):

    def feature3(self):
        print('We have also feature #3 in class B.')

    def feature4(self):
        print('Feature 4? What else? Class B FTW')


#class C(A, B):
class C(B):

    def feature5(self):
        print('Feature 5 from class C')


a1 = A()
b1 = B()
c1 = C()

a1.feature1()
a1.feature2()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1.feature5()
