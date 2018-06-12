
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print (os.name)
  
  # Check for item existence and type
  print ("Item exists: " + str(path.exists("myFile.txt")))
  print ("Item is a file: " + str(path.isfile("myFile.txt")))
  print ("Item is a directory: " + str(path.isdir("myFile.txt")))
  
  # Work with file paths
  print ("Item's path: " + str(path.realpath("myFile.txt")))
  print ("Item's path and name: " + str(path.split(path.realpath("myFile.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("myFile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("myFile.txt")))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("myFile.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
  main()
