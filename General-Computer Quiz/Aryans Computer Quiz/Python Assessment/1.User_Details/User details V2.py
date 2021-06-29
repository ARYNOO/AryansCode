def greet():              
    global name 
    while True:
        name = input("Please enter your name here : ")
        if name.replace(' ','').isalpha(): #by using .isalpha the program will only allow alphabets!
            break 
        print("The data type you have used is invalid data type. (Please enter your name in alphabets only.)\n")

#def functions, Calling the functions which will now work as intended
greet()
rounds()
rule()
status()
