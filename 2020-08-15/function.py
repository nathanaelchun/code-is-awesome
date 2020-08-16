def print_my_age(age):
    print("You are "+str(age))


def combi_ages(age_1, age_2):
    combi = int(age_1)+int(age_2)
    return combi


if __name__ == "__main__":
    answer_1 = input("What is your age?:")
    answer_2 = input("What is your friend's age?:")
    print_my_age(answer_1)
    print_my_age(answer_2)
    combi = combi_ages(answer_1,answer_2)
    print("Your combined age is "+str(combi))
