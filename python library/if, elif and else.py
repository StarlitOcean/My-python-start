#if can be set alone in a function

playerChosenNumber = 10

#checks is the number is 10
if playerChosenNumber == 10:
    print("the number is ten")

#Comparasons are always booleans in the background
print(playerChosenNumber == 10, "because this is True")

if playerChosenNumber == 4:
    print("its a four")

#elif stands for Else if, python uses Elif but other languages like
# C# use "else if"
elif playerChosenNumber == 10:
    print("its a ten")

#now after the IF function there can be as many Elif's as you want.
#you can also let them away

#the else is when nothing works else

playerNumb = 20

if playerNumb == 4:
    print("its a four")
elif playerNumb == 10:
    print("its a ten")
else:
    print("cannot be recognised")

#the else takes anything else that isn't in the if nor the elif.

#in the comparasons there are multiples signs you can use

# == | equals
# >= | bigger or equals
# <= | smaller or equals
# >  | bigger
# <  | smaller
# != | not equals
#-------------------------------------------------------------------------
# is | same variable
# not| being a word for inverting the effects (can be an extra with "is")

if True is not False:
    print(True is not False)

#at some cases python comparasons can be almost written in english. :D

if 5 > 3:
    print("five bigger than three")


    
