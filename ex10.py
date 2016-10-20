#In ex9 Zed showed how to make a string that goes across multiple lines
#The first way was using \n which creates a new line by putting
#a new line character into the string at that point

# The backslash \ character encodes difficult to type characters
#into a string. There are various "escape sequences" available
#for different characters you might want to use

#Here's one example and it's important
#Escaping a single quote or double quote. for instance if you
#write "I "understand" Joe." then python will get confused because
#it will think the double quote around understand ends the string
#EX:
# "I am 6'2\" tall." esacpe double-quote inside string
# 'I am 6\'2" tall.' escape single-quote inside string

#The last way is to use triple-quotes """ which works like a string
#you can also put as many line of text as you want until you
#type """ again

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non \fa \fl \fi \fn \fe."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = '''
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# '''

# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat

# while True:
# 	for i in ["/","--","|","\\","|"]:
# 		print "%s\r" % i,

x = "%r, %r, %s, %s"
y = ("\"double-quote\"",'\'single-quote\'','\'single-quote\'',"\"double-quote\"")

print x % y