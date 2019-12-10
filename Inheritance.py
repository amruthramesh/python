class A:
    def __init__(self):
        print ("Class A init")

    def featureA(self):
        print ("Class A Feature")

class B:
    def __init__(self):
        print ("Class B init")

    def featureB(self):
        print ("Class B Feature")

class C(A, B):
    def __init__(self):
        super().__init__()
        print ("Class C init")

    def featureC(self):
        print ("Class C Feature")
        super().featureB()

c = C()
c.featureC()


# Output
    # Class A init                                                                                                                                                
    # Class C init                                                                                                                                                
    # Class C Feature                                                                                                                                             
    # Class B Feature  