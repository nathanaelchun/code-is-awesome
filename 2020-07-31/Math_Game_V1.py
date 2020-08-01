import random
answer = input("Math Game Chose Which Game You Want To Play: Muliplication,Addition,Subtraction,Division:")
if answer == "Addition":
    number1 = random.randint(0,20)
    number2 = random.randint(0,20)
    numberstr1 = str(number1)
    numberstr2 = str(number2)
    correctadditionanswer = number1+number2
    correctadditionanswerstr = str(correctadditionanswer)
    additionanswer = input("what is "+numberstr1+"+"+numberstr2+":")
if additionanswer == correctadditionanswerstr:
    print("correct!")
else:
    print("The correct answer is "+correctadditionanswerstr)
