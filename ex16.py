#list of commands lord Zed wants me to remember:
# close -- Closes the file. Like File->Save.. in your editor
# read -- Reads the contents of the file. You can assign the result
# readline -- Reads the contents of the file. You can assign the 
# 			  result to a variable 
# truncate -- Empties the file. Watch out if you care about the file
# write('stuff') -- Writes "stuff" to the file

from sys import argv
#parameters for argv, meaning two arguments are required at the commmand line
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#halts before the file is erased and waits for the user to hit
#return or CRTL-C
raw_input("?")

print "Opening the file..."
#opens the file, second arg 'w' is used for write, r for read
#r+ for read and write
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#deletes all content previously in file
#only used here to demonstrate truncate
#not necessary with open(str, 'w') already tell you to write
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
#re-opens file to read it after it has been changed
read_new_text = open(filename, 'r')
print ""
#prints out the content of the what the computer reads
print read_new_text.read()
