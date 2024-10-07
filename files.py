def main():  
  # Open a file for writing and create it if it doesn't exist
    fil = open("my_file.txt", "w+")
    

  # write some lines of data to the file
    for i in range(50):
        fil.write("Student with Id  %d\r\n" % (i+1))
  
  # close myFile
    fil.close()
    
if __name__ == "__main__":
    main()