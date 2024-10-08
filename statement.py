# Indentation matters in python when using if statement.

# Python does not have support for higher-order conditionals like "switch-case" in other languages


def main():
  a, b = 20, 20
  
  # conditional flow uses if, elif, else  
  if a < b:
    out = "a is less than b"
  elif a == b:
    out = "a is equal to b"
  else:
    out = "a is greater than b"
  print (out)

  out = "a is less than b" if (a < b) else "a is greater than or equal to b"
  print (out)
  

if __name__ == "__main__":
  main()
