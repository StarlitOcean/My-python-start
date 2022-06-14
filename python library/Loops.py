#there are 2 types of loops
#the while and the for

#the while has a very similar syntax (Grammar) as an if function
#except it loops until its False.

loopTillTen = 0

while loopTillTen != 10:
    loopTillTen += 1
    print(loopTillTen, "another loop")
    print(loopTillTen != 10)

#just for the format
print("-------------new Example------------")

#while can also be put forever but with a break function be stopped

alsoLoopTillTen = 0

while True:
    alsoLoopTillTen += 1
    if alsoLoopTillTen == 5:
        continue
        #continue will skip the current loop
    print(alsoLoopTillTen, "works!")
    if alsoLoopTillTen == 10:
        print("five was skipped")
        break
        #break function can stop the loop
    
#just for the format
print("-------------new Example------------")

#the other loop if the FOR loop

for each in range(10):
    print(each, "grows")

#range is a special function for itself

print(list(range(10)), "another use for range()")

#just for the format
print("-------------new Example------------")

#the for loop can also be used on strings and lists.

allObjects = ["this", "is", "a", "sentance"]

for each in allObjects:
    print(each, "<== another list object")



    
