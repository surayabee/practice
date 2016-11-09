my_first_name = "Suraya!"
print "Hello Kai and " + my_first_name

# Number string interpolation
age = 22
print "My name is " + my_first_name + "and I am " + str(age)

To Print Strings
print "word"

To Print Variables
the_machine_goes = "Ping!"
print the_machine_goes

To create a new line horizontally
print "\n"

To get the length (the number of characters) of a string
parrot = "Norwegian Blue"
print len(parrot)

To get rid of all the capitalization in your strings
parrot = "Norwegian Blue"
print parrot.lower()

To capitalize all the characters in the string
parrot = "norwegian blue"
print parrot.upper()

To turn non-strings into strings = The str() method
pi = 3.14
print str(pi)

String Concatenation aka Combining Strings Together
print "Spam " + "and " + "eggs"

Explicit String Conversion - Combining a string with a non-string
print "I have " + str(2) + " coconuts!"
    print "I have " + 2 + " coconuts!"

print "The value of pi is around + 3.14
    print "The value of pi is around " + str(3.14)

Name: String Formatting with % part1
Purpose: To print a variable with a string
Scrypt:
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
Result: Let's not go to Camelot. 'Tis a silly place.

Name: String Formatting with % part2
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)




Error That White Space Is Off
IndentationError: expected an indented block

Below Is Wrong
def spam():
eggs = 12
return eggs

print spam()

Below Is Right (4 spaces before "eggs" and "return")
def spam():
    eggs = 12
    return eggs

print spam()
