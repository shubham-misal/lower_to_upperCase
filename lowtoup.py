while True:
  #lower case to upper case
  inp=str(input("\nEnter anything only in lowercase:\n>>"))
  ln=0
  for a in inp:
    ln=ln+1
  for i in range(ln):
    cb=ord(inp[i])
    cf1 = cb-32
    cf1 = chr(cf1)
    print(cf1,end="")
    # or 
    """ global con
    con=(cb>=97 and cb<=123)
    try:
      if(con==True):
        cf1 = cb-32
        cf1 = chr(cf1)
        print(cf1,end="")
    except ValueError:
      pass
      if(con==False):
        print("Enter only uppercase")
        break """