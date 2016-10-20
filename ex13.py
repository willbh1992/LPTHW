#calles an import, rather than give you all the modules(libraries) 
#at once python asks you to say what you plan to use
#keeps program small and also adds readabilty for others

#argv is argument variable, this varibale holds the arguments
#you pass to your Python script when you run it
from sys import argv
#Unpacks argv so it assigns whatever is inside argv to the four
#variables below
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
