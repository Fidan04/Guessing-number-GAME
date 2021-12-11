import random

def play_game():
    number=random.randint(1, 9999) #numbers between 1 and 999
    guess= None
    tries=0  
    while guess != number:
        guess=int(input("Guess a number:"))

        if guess == 0:
            print("You are going to quit game")
            a=input("Are you sure? yes/no >>")
            if a=="yes":
                print("Bye")
                break
            else:
                print("OK let's continue")
        

        if guess > number:
            print("Your guess > number")
        if guess < number:
            print("Your guess < number")

        if guess == number:
            print("Your guess = number. You win!")
            break
        else:
            print("Try again")
        tries+=1
    print("The number of tries is {0}".format(tries))

play_game()

def Start():
    global step   #we should write global 
    global s      #to use these variables 
    global e      #in other function too
    step=0
    s=1   #this is the smallest number
    e=9999   #and this is the biggest number
    print("Guess a number between {0} and {1}\n".format(s,e))

    Find()
     

def Find():
    global step
    global s
    global e
    step+=1

    number=random.randint(s,e)

    print("Step {0}: Is your guess number {1}? \n".format(step,number))

    answer=input("If it is too small <, too large >, found = :")

    if answer == "=":

        print("Your guess=number={0}. And you found it for {1} steps".format(number, step))

        choise=input("Do you want to play again? Or let the machine play. yes/no>>")
        if choise=="yes":
            play_game()
        if choise=="no":
            Start()
            

    elif answer== ">":
        e=(number-1)
        Find()
    elif answer== "<":
        s=(number+1)
        Find()

Start()