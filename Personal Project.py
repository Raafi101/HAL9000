#Personal Project



import time
import turtle
import random
import operator



#Definitions
alist = ["1) Drawing with turtles" , "2) Math challanges" , "3) Turn off"]



#Commonly used lines of string
HAL9000 = ("I am a HAL 9000 computer, an Artificial Intelligence. HAL stands for " \
           "Heuristically programmed ALgorithmic computer.")



#Math Challange code
def mc():
    ops = ['+','-','*','/']
    def randomCalc():
        ops = {'+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':operator.truediv}
        num1 = random.randint(0,100)
        num2 = random.randint(1,100)
        op = random.choice(list(ops.keys()))
        answer = ops.get(op)(num1,num2)
        print('What is {} {} {}?\n'.format(num1, op, num2))
        return answer
    def askQuestion():
        answer = randomCalc()
        guess = float(input())
        return guess == answer
    print("Here you will be challenged in arithmitic with random numbers and operations.")
    time.sleep(1)
    print("You will answer 10 questions and then be given a score.")
    score = 0
    for i in range(10):
        correct = askQuestion()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
    print(" ")
    print('Your score was {}/10'.format(score))
    print(" ")
    again = str(input('Would you like to play again? Type "Yes" or "No". '))
    if again == "Yes" or again == "yes":
        print(" ")
        mc()
    elif again == "No" or again == "no":
        print(" ")
        choose()



#Drawing with turtles code                
def dwt():
    print('Type "A" and "D" to choose the direction you want to turn. ')
    time.sleep(1)
    print('Then enter the number of degrees you would like to turn. ')
    time.sleep(1)
    print('If you dont want to turn, type "0" degrees. ')
    time.sleep(1)
    print('Then type in the number of steps you would like to take forward. ')
    time.sleep(1)
    print('If you wish to return back to the main menu, type "End" when it ask you for a direction. ')
    time.sleep(1)
    print(" ")
    HalT = turtle.Turtle()
    color = str(input("Enter a color for your turtle : "))
    HalT.color(color)
    def dwtM():
        i = 1
        while i > 0:
            d = str(input('Enter "A" or "D" to choose direction : '))
            if d == "A" or d == "a" or d == "D" or d == "d":
                t = float(input('Enter the number of degrees you would like to turn. Type "0" if you do not wish to turn : '))
                s = float(input('Enter how many steps you wish to take : '))
                if d == "A" or d == "a":
                    HalT.left(t)
                elif d == "D" or d == "d":
                    HalT.right(t)
                HalT.forward(s)
            elif d == "End" or d == "end":
                print(" ")
                choose()
            else:
                print("That's not a valid direction!")
                dwtM()
    dwtM()


    
#Prompts user to turn Hal on
def power():
    power.on = str(input('Type "On" to turn on your HAL9000. '))
    if power.on == "on" or power.on == "On" or power.on == "ON" or power.on == "on " or power.on == "On " or power.on == "ON ":
        greeting()
    else:
        power()

        

#The first few lines greeting the user. Asks user for name
def greeting():
    print("Hello! ")
    time.sleep(1)
    greeting.user = str(input("What is your name?: "))

    

#replies back using users name. Tells about activities
def reply1():
    print("Nice to meet you, " + greeting.user + ".")
    time.sleep(1)
    print("My name is Hal.")
    time.sleep(1)
    print(HAL9000)
    time.sleep(3)
    print("You, " + greeting.user + ", are my new owner. I have math games and puzzles for you to participate in.")
    time.sleep(2)
    print("Here are a few things you can do with me...")
    time.sleep(1)
    print(" ")
    

    

#Prompts user to choose an activity
def choose():
    for x in alist:
        print(x)
        time.sleep(1)
    print(" ")
    choose.choice = str(input("Choose what you want to do by writing the name or the number of the activity: "))
    print(" ")
    if "1" == choose.choice or "1)" == choose.choice or "drawing with turtles" == choose.choice or "Drawing with turtles" == choose.choice:
        dwt()
    elif "2" == choose.choice or "2)" == choose.choice or "math challenges" == choose.choice or "Math challanges" == choose.choice:
        mc()
    elif "3" == choose.choice or "3)" == choose.choice or "Turn off" == choose.choice or "turn off" == choose.choice:
        print("Goodbye " + greeting.user + "!")
        print(" ")
        power()
    else:
        print("That isn't a valid choice!")
        print(" ")
        choose()


        
#Main function
def main():
    power()
    time.sleep(1)
    reply1()
    choose()
       
if __name__ == "__main__":
    main()
