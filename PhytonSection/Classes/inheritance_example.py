

class Class1:

    def __init__(self, cls1_input_1):
        print("__init__ of Class 1")
        self.prop_cls1 = 10
        self.cls1_in_1 = cls1_input_1
        print(self.cls1_in_1)
    
    def method1Class1(self):
        print("Method 1 Class 1")

class Class2(Class1):
    
    def __init__(self, cl1in1, cl2in1):
        super().__init__(cl1in1)
        print("__init__ of Class 2")
        self.cl2in1 = cl2in1

    def method1Class2(self):
        print("Method 1 Class 2")

obj2 = Class2('abc', 'xyz')

obj2.method1Class2()
obj2.method1Class1()

print(obj2.cls1_in_1)