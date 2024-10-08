#A loop statement allows us to execute a statement or group of statements multiple times.


def main():
  var = 0
  
  # define a while loop
  while var < 5:
     print (var)
     var = var + 1
  

  # define a for loop
  for var in range(5,10):
    print (var)
    
  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # use the break and continue statements
  for var in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (var)
  
  #using the enumerate() function to get index 
    
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)
  
if __name__ == "__main__":
  main()
