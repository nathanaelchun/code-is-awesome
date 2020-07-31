point = 0
earned = 1
upgrade = 1
while point <100:
    if point <=-1:
        print("Congratulations!")
        print()
        print()
        print("You are a cheater!")
        print()
        print()
        print("lol")
        exit(0)
    Str_point = str(point)
    answer = input("you have "+Str_point+" points."+" to get points enter get to increase the amount of points per entering get enter upgrade. ")
    if answer =="get":
        point = point + earned
    if answer =="upgrade":
        point = point-5
        earned = earned + upgrade
print("Congratulations you finally beat the Game!")
exit(0)