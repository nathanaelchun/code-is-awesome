# import random
# x = [1, 2, 3]
# y = 0
# m = 10
# o = 5
# while y < o:
#     x.append(random.randint(0,10))
#     y = y+1
# for f in range(1,m):
#     x.append(random.randint(0,10))
# total = m+y+2
# for k in range(0,total):
#     print(k,x[k])

import random
x = [1, 2, 3]

y = 0
m = 10
o = 5
while y < o:
    x.append(random.randint(0,10))
    y = y+1
for f in range(1,m):
    x.append(random.randint(0,10))
for k in range(len(x)):
    print(k,x[k])


questions = ["what's your name?", "what's your age?", "where do you live?"]

for i in range(len(questions)):
    print(questions[i])

for i in questions:
    print(i)
    