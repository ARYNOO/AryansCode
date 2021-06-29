from random import shuffle #Shuffle asks questions randomly each time

#lines used for aesthetics
lines1 = ('===============================')
lines2 = ('=========================================================')
lines3 = ('===============================================================================')

#introduction and disclaimer
print("\nTHIS IS A GENERAL KNOWLEDGE GAME QUIZ MADE FOR MY SCHOOL PROJECT. THIS PROGRAM IS MADE TO TEST YOUR GENERAL KNOWLEDGE ON COMPUTERS!")
print(lines3+lines2,"\nLet's Begin!")


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

    
#using dictionary and lists to store questions and right answer for the quiz

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


q_number=[i for i in range(len(gkquiz))] #asking the user if they want to play the quiz again.
shuffle(q_number)

index = 0
score = 0
optnum = 0

   

#def functions, Calling the functions which will now work as intended
greet()
rounds()
rule()
status()



while True:
    while r>0:#using for range 
        data = gkquiz[q_number[0]]
        q = data[0]
        data = data[1]
        answer = data['answer']
        option = data['option']

        print(q)#printing questions
        print(option)#printing options
        while True: #while is a function and it can be combined with boolean as below
            user_answer = input("Please enter your answer here : ").lower().replace(' ','')
            if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
                if user_answer == answer: 
                    print("NICE ONE!")
                    score +=1 #Showing score and it will increase as the user gains more.
                    print("Your score is",score)
                else:

                    print("Sorry the option you have chosen is not right. The answer is ",answer)
                    print("Your score is",score)
                    

                del q_number[0] #using del so question wont repleat ever
                r-=1
                break
            else:
                print("Please enter the alphabet for the chosen option")

                print(name,"Your score is ",score,"out of",total) #Show the score and stats for the end of the quiz.
    print("The precentage of the score is",(round(score/total*100,2)),"%") #showing percentage of the score for enduser
    print("You have compleated the quiz, Welldone.")
    print("\nThank you for playing! - this quiz was made by ARYAN")
    if score == total:
        print('!'*7)
        print("goodjob!")
        print('!'*7)
    print('='*7)
    if input('Do you want to play again enter y to continue or any other key to exit: ') in ['Y','Yes','y','yes','YES','Yss','ye','YEE']:#asking if the users to play again.
        print('='*7)
        rounds()
    else:
        exit()

