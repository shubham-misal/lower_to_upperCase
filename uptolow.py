while True:
  # upper case to lower case
  inp1 = str(input("\nEnter anything only in uppercase:\n>>"))
  ln1 = 0
  for a1 in inp1:
    ln1 = ln1+1
  for i1 in range(ln1):
    # this will replace "" blank-space  with @
    cb1 = ord(inp1[i1])
    cf1 = cb1+32
    cf1 = chr(cf1)
    print(cf1,end="")
    # or 
    #this will cut the blank space from the string and concatinate the string and print it
    """ con=(cb1>=65 and cb1<=91)
    try:
      if(con==True):
        cf1 = cb1+32
        cf1 = chr(cf1)
        print(cf1,end="")
    except ValueError:
      if(con==False):
        print("Enter only uppercase")
        break """