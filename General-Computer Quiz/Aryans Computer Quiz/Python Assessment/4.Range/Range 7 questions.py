#create a function, the variable name is rounds
def rounds():
  while True:
    r = int(input("how many questions do you want? between 1-7: "))
    #determine if r is within range
    if 0<r<=7:
      break

 #if not then code loops
    else:
      print("Please enter numbers 1-7 only")

#call function
rounds()


