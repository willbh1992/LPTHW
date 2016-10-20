#Zed Defines Strings:
#A string is usually a bit a of text you want to display to someone
#or "export" out of the program you are writing. Python knows
#you want something to be a string when you put either " (double-quotes)
#or ' (single-quotes) around the text. You saw this many times
#with your use of print when you put text you want to fo inside
#the string inside " or ' after the print to print something

#A string may contain the format characters you have discovered
#so far. You simply put the formatted variables in the steing, and
#then a % (percent) chracter, followed byt he variable. The only catch
#is that if you want multiple formats in your string to print multiple
#variables, you need to put them inside ( ) seperated by ,(commas) .
#It's as if you were tellng me to buy you a list of items from
#the store and you said, "I want milk, eggs, bread, and soup."
#Only as a programmer we say:
#"(milk, eggs, bread, soup)"


#assigns string to x which ocntains a string formatter (%d) that is refernced with %10
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#print x then y
print x
print y
#assign nested string that calls x which is alo a nested string
print "I said: %r." % x #1
#creates a nested string with %s that calls y which is also a nested string
print "I also said: '%s'." % y #2
#assigns variable to boolean value false
hilarious = False
#assigns a string and a string formatter %r to variable
joke_evaluation = "Isn't that joke so funny?! %r" #3
#prints joke evaluation and calls the string formatter %r for %hilarious
print joke_evaluation % hilarious #4
#assigns variables to strings
w = "This is the left side of..."
e = "a string with a right side."
#Concatenates the strings attached to variales w and e
print w + e

#additional notes:
# %d will format a number for display
# %s will insert the string representation of the object (i.e. str(o))
# %r will insert the canonical string representation of the object(i.e. repr(o))
