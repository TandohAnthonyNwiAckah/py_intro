#
# Shell methods.
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    
  # Duplicate of an existing file
  if path.exists("myFile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("myFile.txt");
        
    # # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # # Use the shell to make a copy of the file
    shutil.copy(src,dst)
    
    # # copy over the permissions, modification times, and other info
    shutil.copystat(src, dst)
    
    #  Rename the original file
    os.rename("myFile.txt", "myFile.txt")
    
    # Backup Archive
    root_dir,tail = path.split(src)
    shutil.make_archive("backup", "zip", root_dir)

    # Shell ZIP files
    with ZipFile("Shell.zip","w") as newzip:
      newzip.write("myFile.txt")
      newzip.write("myFile.txt.bak")
      
if __name__ == "__main__":
  main()
