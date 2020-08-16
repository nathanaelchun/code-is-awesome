def multiplication(number_1, number_2, number_3):
    answer = int(number_1)*int(number_2)*int(number_3)
    return answer


if __name__ == "__main__":
    answer_1 = input("Type in a number you want multiplied: ")
    answer_2 = input("Type in a number you want multiplied: ")
    answer_3 = input("Type in a number you want multiplied: ")
    answer = multiplication(answer_1, answer_2, answer_3)
    print("answer is "+str(answer))
