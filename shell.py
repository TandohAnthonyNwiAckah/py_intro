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
  if path.exists("my_file.txt"):
    # get the path to the file in the current directory
    src = path.realpath("my_file.txt");
        
    # # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # # Use the shell to make a copy of the file
    shutil.copy(src,dst)
    
    # # copy over the permissions, modification times, and other info
    shutil.copystat(src, dst)
    
    #  Rename the original file
    os.rename("my_file.txt", "my_file.txt")
    
    # Backup Archive
    root_dir,tail = path.split(src)
    shutil.make_archive("backup", "zip", root_dir)

    # Shell ZIP files
    with ZipFile("shell.zip","w") as newzip:
      newzip.write("my_file.txt")
      newzip.write("my_file.txt.bak")
      
if __name__ == "__main__":
  main()
