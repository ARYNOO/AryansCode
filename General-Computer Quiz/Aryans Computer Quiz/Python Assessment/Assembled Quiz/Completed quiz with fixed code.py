from random import shuffle#imports random for question
#varibles
index = 0
score = 0
optnum = 0
#Using dictionary for questions and for the right answers
gkquiz =[
[
    "\nWhat cpu uses the LGA socket type?",
    {'answer':'a','option':'a)intel\nb)AMD\nc)Exnoys\n'}
    ],
[
    "\nWhat is the 24pin from the powersupply used for?",
    {'answer':'a','option':'a)Motherboard Power\nb)CPU power\nc)Graphics card power\nd)USB power\n'}
     ],
[
    "\nWhat is a M.2 SSD for?",
    {'answer':'b','option':'a)Run games\nb)Fast Storage\nc)For display\nd)For Gaming\n'}
     ],
[
    "\nWhich CPU brand uses pins on their cpus?",
    {'answer':'c','option':'a)EXNOYS\nb)APPLE\nc)AMD\nd)INTEL\n'}
     ],
[
    "\nWhat does RAM mean?",
    {'answer':'a','option':'a)Random Access Memory\nb)Random Access memus'}
     ],
[
    "\nWhat is a CPU used for",
    {'answer':'a','option':'a)processes the basic instructions that drive a computer\nb)Gaming\nc)Powers the pc\nd)Stores software\n'}
     ],
[
     "\nWhat Socket does AMD use for RYZEN cpus?",
    {'answer':'c','option':'a)AM3\nb)LGA\nc)AM4\nd)AM5\n'}
     ],
]
#User defined functions
#using functions to ask name and using .isalpha is used so the program only allows characters.
def greet():              
    global name 
    while True:
        name = input("Please enter your name here : ")
        if name.replace(' ','').isalpha():
            break 
        print("The data type you have used is invalid data type. (Please enter your name in alphabets only.)\n")


#Asking user if they want to see rules.
def rule():
    rule = input("\nDo you want to read the rules or continue without the rules? \nPress Y to learn the rules or any other key to continue without knowing the rules : ").lower()
    rule = rule.replace(' ','')
    if rule == "y" or rule == "yes" or rule == "okay":
        print("\nThe quiz is easy \n1. Enter the answer in a,b,c,d.\n2. You are not allowed to use cheat.")
        print("You may continue.")

#Asking for STATUS, if they want to play.
def status():
    status = input("\nAre you ready to play? :  ").lower()
    status = status.replace(' ','')
    if status == "y" or status == "yo" or status == "yes":
        print("\nThank you!")
    else:
        print("\nThank you, please join again when you are ready!.")
        exit()
#this is a function that asks the user to enter the rounds they want to play
def rounds():
    global r , total
    while True:
        try:
            r = int(input("How many rounds do you want to play? : "))
            if 0<r<=7:#this only allows 0-10 
                break
            else:
                print("ERROR 1-7 only")
        except:
            print('Please enter rounds in numbers only (The max number of rounds is 7!)')
               
        
    total=r

#Print functions such as lines, decorators etc.

print("======*==============================*======")#Welcome the user once they're ready to take the quiz
print("------------------- Welcome to Computer Quiz --------------------")
print("--------------------- Made by Aryan Narayan ----------------------")
print("======*==============================*======")
greet() #Call the functions
rounds()
rule()
status()



shuffle(gkquiz)#shuffle for random questions. 



while r>0:
    data = gkquiz[0]
    i = data[0]
    data = data[1]
    answer = data["answer"]
    option = data['option']


    print(i)#printing questions
    print(option)#printing options

            #Main Routine
    while True:#while True loop
        useranswer = input("Enter your answer here please : ") #asking for inputs
        if useranswer == 'a' or useranswer == 'b' or useranswer == 'c' or useranswer == 'd':#this is user answer where there wide range of option to pick 
            if useranswer == answer:#checking user answer 
                print("=====================")
                print("Correct!")
                print("=====================")
                score += 1
                print("*********************************")
                print("Your score is",score         )#printing score 
                print("*********************************")
            else:
                print("============================= ")
                print("your answer is wrong !")#correcting the users by show them the answer and show the score didn't increase
                print(" The answer is",answer  )#showing right answer
                print("*******************************")
                print("  You score is",score           )
                print("============================= ")
            del gkquiz[0] #deleting the question to not repeat the question 
            r-=1
            break#breaking the loop
        else:
            print("===========================")
            print("Please enter a,b,c,or d")#this happens if the user inputs characters or if they input blank.
            print("===========================")


                                
print("\nYou've scored",score,"out of",total,"questions")#showing the result after the quiz end.
print("your score in percentage",round(score/10*100,2),"%")#show round score.
print("You have ended the quiz succesfully, Congrats.")#thanks end users
print("********************************************************************************************")
print("\nIf there is anything that has affected you in anyway email me 19158@students.mrgs.school.nz")#This is a disclaimer if i have done any harm or offened anyone with anything to let me via email.
print("********************************************************************************************")
print("You have ended the quiz succesfully, Congrats.")
exit()#exit to finish the quiz
