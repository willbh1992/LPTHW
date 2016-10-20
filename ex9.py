# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#Study Drills
#Added an extra double quote at the end of line 14 gave error:
#SyntaxError: EOL while scanning straight literal

#New ideas
# \n creates a new line and it does not work if you use %r
#%r returns the most efficient output of what you wrote
#if you want to maintain formatting for text string use %s
#use %d for integers