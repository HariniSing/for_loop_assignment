# Basic - Print all integers from 0 to 150.
print("Print all integers from 0 to 150")
for i in range(0,151):
    print(i)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Print all the multiples of 5 from 5 to 1,000")
for i in range(5,1001,5):
    print(i)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("Print integers 1 to 100. If divisible by 5, print Coding instead. If divisible by 10, print Coding Dojo.")
for i in range(1,101):
    if i%5==0:
        print("Coding")
    if i%10==0 and i%5==0:
        print("Dojo")
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print("Add odd integers from 0 to 500,000, and print the final sum")
add=0
for i in range(1,500000,2):
    add=add + i
print (add)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours. 
print("Print positive numbers starting at 2018, counting down by fours")
number = 2018
while number > 0:
    print (number)
    number = number - 4

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flexibleCount(lowNum,highNum,mult):
    for i in range(lowNum,highNum):
        if i%mult == 0:
            print(i)
flexibleCount(2,9,3)