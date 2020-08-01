import random
problem_done = 0
problem_right = 0
problem_wrong = 0
answer = input("Math Game Chose Which Game You Want To Play: Muliplication,Addition,Subtraction,Division:")
while problem_done <10:
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
        problem_done = problem_done + 1
        problem_right = problem_right + 1
    else:
        print("The correct answer is "+correctadditionanswerstr)
        problem_done = problem_done + 1
        problem_wrong = problem_wrong + 1
    problem_right_str = str(problem_right)
    problem_wrong_str = str(problem_wrong)
    problem_done_str = str(problem_done)
print("Congratulations! You Got "+problem_right_str+" right "+"and "+problem_wrong_str+" wrong "+"So you got "+problem_right_str+" out of "+problem_done_str+".")
