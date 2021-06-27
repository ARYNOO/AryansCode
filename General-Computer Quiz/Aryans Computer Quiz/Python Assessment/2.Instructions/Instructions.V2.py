#the variable will be called ARN
#create a function
def instructions():
            #create while loop
            while True:
                        #ask for user input
                        inst = input("""
Would you like to read the instructions?
a)yes
b)no
Enter here: """)
                        #determine if user wants to read instructions
                        if inst == "yes" or inst == "y" or inst == "A" or ARN == "a":
                                    print("The rules are simple. Answer the multi choice questions by entering (a/b/c/d). For every question you get right you earn a point.")
                                    break
                        if inst == "no" or inst == "n" or inst == "B" or inst == "b" :
                                    break
#call function
instructions()
