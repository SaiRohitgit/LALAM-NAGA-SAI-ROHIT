def main():
  inp = int(input("Enter the number:"))
  if inp % 2== 0:
    inp= inp-1
  count = 0
  num = 1
  while count<inp:
    print(num,end="")
    if count<inp-1:
      print(",",end="")
    num+=2
    count+=1
  print()
if __name__=="__main__":
  main()
