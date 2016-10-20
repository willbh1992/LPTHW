# Most of what software doe is the following
# 1. Take some kind of input from a person
# 2. Change it.
# 3. Print out something to show how it changed

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

print '''
Four is the cosmic number
Any integer can be reduced to or exapnded to it
It is easiest to solve if you use numbers between 0 and 10
Did not write the code for it but it can compute any integer beyond that range
'''
while True:
	print "Enter integer value between 0 and 10"
	number = int(raw_input())
	if number == 1 or number == 2 or number == 6 or number == 10:
		print "%s becomes 3 becomes 5 becomes 4 and 4 is always 4" % number
	if number == 0 or number == 4 or number == 5 or number == 9:
		print "%s becomes 4 and 4 is always 4" % number
	if number == 3 or number == 7 or number == 8:
		print "%s becomes 5 become 4 and 4 is always 4" % number
	print "Have you figured it out?"
	print "Give up?"
	print '''
	If you figured it out or gave up then type y for solution
	If you want to keep guessing type n:
	'''
	response = raw_input()
	if response == 'y':
		print '''
		Four is cosmic because if you count out the letters in an
		integer value and then move to the number counted out you
		will eventually reach four which is always four because it
		has four letters
		'''
		break


		
