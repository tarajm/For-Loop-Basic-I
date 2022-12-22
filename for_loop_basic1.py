
#Basics

for x in range(0,151):
    print(x)

#Multiples of Five

for x in range(5,1001,5):
    print(x)

#Counting, the Dojo Way

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


#Whoa. That Sucker's Huge

sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)    



#Countdown by Fours

for i in range(2018, 0, -4):
    print(i)


#Flexible counter

low_num = 2
high_num = 9
mult = 3

for i in range(low_num, high_num +1):
    if i % mult == 0:
        print(i)
