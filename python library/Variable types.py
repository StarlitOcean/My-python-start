#as usual integers take also good variable names.

textContent = "hello world"
number = 9

#Variable types can be viewed with "type()" function

print(type(textContent), "string")
print(type(number), "integer")

#usually type isn't used that much but it has its uses to see what something is:
#example:

unknownContent = open("hello world.py", "r") #unknown function
unknownContent.close()#ignore that

print(type(unknownContent), "we know from TextIOWrapper that its an open file")

#numbers with coma are FLOATS.

containsThree = 3.21

print(type(containsThree), "which is a float")

#True and False are BOOLEANS.

thisIsTrue = True

print(type(thisIsTrue), "which is a BOOLEAN")

#In the variable types theres also something called a "List".

containsAllOtherTypes = ["hello world", 4, 3.21, True]

print(type(containsAllOtherTypes), "which is a list")

#lists can contains multiples objects and thier lenght can be checked
#using the "len()" function

print(len(containsAllOtherTypes), "it contains 4 objects")

#lenght can also be used in specificly Strings.

textHello = "hello world"

print(len(textHello), "hello world contain 11 letters")





