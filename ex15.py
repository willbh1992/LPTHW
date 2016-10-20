#imports argv from module sys
from sys import argv
#sets number of arguments for argument vector
script, filename = argv
#assigns the called file to variable txt via the open function
txt = open(filename)
#prints string including name of file
print "Here's your file %r:" % filename
#tells python to read or display text inside file
print txt.read()
#asks you to retype filename
print "Type the filename again:"
#prompts user to type in filename
file_again = raw_input("> ")
#works the same as line 6
txt_again = open(file_again)
#works the same as line 10
print txt_again.read()