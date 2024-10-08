# A class is a code template for creating objects. 
# Objects have member variables and have behaviour associated with them. I


class MyClass:
    def method1(self):
        print("My Class method1")

    def method2(self, sth):
        print("My Class method2: " + sth)

class AnotherClass(MyClass):
    def method2(self,sth):
        print("Another Class method2")

    def method1(self):
        MyClass.method1(self)
        print("Another Class method1")


def main():
    c = MyClass()
    c.method1()
    c.method2("This is a string")
    c2 = AnotherClass()
    c2.method1()


if __name__ == "__main__":
    main()
