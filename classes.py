# A class is a code template for creating objects. 
# Objects have member variables and have behaviour associated with them. I


class myClass():
  def method1(obj):
    print ("myClass method1")
    
  def method2(obj, sth):
    print ("myClass method2: " + sth)
    
class anotherClass(myClass):
  def method2(obj):
    print ("anotherClass method2")
    
  def method1(obj):
    myClass.method1(obj);
    print ("anotherClass method1")
      
        
def main():
  c = myClass()
  c.method1()
  c.method2("This is a string")
  c2 = anotherClass()
  c2.method1()
  
if __name__ == "__main__":
  main()
