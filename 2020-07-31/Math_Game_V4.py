import random
problem_done = 0
problem_right = 0
problem_wrong = 0
answer = input("Math Game Chose Which Game You Want To Play: Multiplication,Addition,Subtraction,Division:")
while problem_done <10:
    problem_done_for_question = problem_done+1
    problem_done_for_question_str = str(problem_done_for_question)
    if answer == "Multiplication":
        number1 = random.randint(0,10)
        number2 = random.randint(0,10)
        numberstr1 = str(number1)
        numberstr2 = str(number2)
        correctmultiplicationanswer = number1*number2
        correctmultiplicationanswerstr = str(correctmultiplicationanswer)
        multiplicationanswer = input("Question"+problem_done_for_question_str+":"+"what is "+numberstr1+"*"+numberstr2+":")
        if multiplicationanswer == correctmultiplicationanswerstr:
            print("correct!")
            problem_done = problem_done + 1
            problem_right = problem_right + 1
        else:
            print("The correct answer is "+correctmultiplicationanswerstr)
            problem_done = problem_done + 1
            problem_wrong = problem_wrong + 1
        problem_right_str = str(problem_right)
        problem_wrong_str = str(problem_wrong)
        problem_done_str = str(problem_done)
    elif answer == "Addition":
        number1 = random.randint(0,20)
        number2 = random.randint(0,20)
        numberstr1 = str(number1)
        numberstr2 = str(number2)
        correctadditionanswer = number1+number2
        correctadditionanswerstr = str(correctadditionanswer)
        additionanswer = input("Question"+problem_done_for_question_str+":"+"what is "+numberstr1+"+"+numberstr2+":")
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
    elif answer == "Division":
        number1 = random.randint(0,20)
        number2 = random.randint(1,2)
        numberstr1 = str(number1)
        numberstr2 = str(number2)
        correctdivisionanswer = number1/number2
        correctdivisionanswerstr = str(correctdivisionanswer)
        divisionanswer = input("Question"+problem_done_for_question_str+":"+"what is "+numberstr1+"/"+numberstr2+":")
        if divisionanswer == correctdivisionanswerstr:
            print("correct!")
            problem_done = problem_done + 1
            problem_right = problem_right + 1
        else:
            print("The correct answer is "+correctdivisionanswerstr)
            problem_done = problem_done + 1
            problem_wrong = problem_wrong + 1
        problem_right_str = str(problem_right)
        problem_wrong_str = str(problem_wrong)
        problem_done_str = str(problem_done)
    elif answer == "Subtraction":
        number1 = random.randint(0,100)
        number2 = random.randint(0,120)
        numberstr1 = str(number1)
        numberstr2 = str(number2)
        correctsubtractionanswer = number1-number2
        correctsubtractionanswerstr = str(correctsubtractionanswer)
        subtractionanswer = input("Question"+problem_done_for_question_str+":"+"what is "+numberstr1+"-"+numberstr2+":")
        if subtractionanswer == correctsubtractionanswerstr:
            print("correct!")
            problem_done = problem_done + 1
            problem_right = problem_right + 1
        else:
            print("The correct answer is "+correctsubtractionanswerstr)
            problem_done = problem_done + 1
            problem_wrong = problem_wrong + 1
        problem_right_str = str(problem_right)
        problem_wrong_str = str(problem_wrong)
        problem_done_str = str(problem_done)
problem_right_percent = problem_right*10
problem_right_percentstr = str(problem_right_percent)
print("Congratulations! You Got "+problem_right_str+" right "+"and "+problem_wrong_str+" wrong "+"So you got "+problem_right_str+" out of "+problem_done_str+".")
print()
print()
print("You got "+problem_right_percentstr+"%")