#Basic

for a in range(0,151,1):
    print(a)

#Multiples of five
print("-------------------------------------------------------")
for e in range(5,1001,1):
    if e%5==0:
        print(e)

#Counting, the Dojo Way
print("-------------------------------------------------------")
for i in range(1,101,1):
    if i%10==0:
        print("Codind Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge
print("-------------------------------------------------------")
sum = 0
for o in range(1,500001,2):
    sum += o
print(sum)

#Countdown by Fours
print("-------------------------------------------------------")
for u in range(2018,0,-4):
    print(u)

#Flexible Counter
print("-------------------------------------------------------")
low = 2
high = 9
mult = 3

for aa in range(low,high + 1):
    if aa % mult == 0:
        print(aa)