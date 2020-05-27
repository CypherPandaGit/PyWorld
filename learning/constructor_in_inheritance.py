class A:

    def __init__(self):
        print('This is in A __init__')

    def feature1(self):
        print('Feature 1 working.')

    def feature2(self):
        print('Feature 2 working too.')


class B(A):

    def __init__(self):
        super().__init__()
        print('This is in B __init__')

    def feature3(self):
        print('We have also feature #3 in class B.')

    def feature4(self):
        print('Feature 4? What else? Class B FTW')

b1 = B()
