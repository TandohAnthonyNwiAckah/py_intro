import urllib.request 

def main():
  # open a connection .
  myUrl = urllib.request.urlopen("http://www.google.com")
  
  # get the result code and print it
  print ("result code: " + str(myUrl.getcode()))
  
  # read the data from the URL and print it
  data = myUrl.read()
  print (data)

if __name__ == "__main__":
  main()
