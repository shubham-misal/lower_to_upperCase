while True:
  #Enter anything and get ==> uppercase, lowercase both
  inp1=str(input("\nEnter anything in both lowercase and upercase:\n>>"))
  ln1=0
  for a1 in inp1:
    ln1=ln1+1
  for i1 in range(ln1):
    cb1=ord(inp1[i1])
  # both can be print at one time it prints some special char before printing the string
    try:
      if(cb1>=97 or cb1<=123 ):
        cf1=cb1-32
        cf1=chr(cf1)
        print(cf1,end="'\t'")
      if(cb1>=65 or cb1<=91):
        cff=cb1+32
        cff=chr(cff)
        print(cff,end="'\t'")
    except ValueError:
      print("INvalid input")