name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

cent_in_inches = 2.54
lbs_in_kg = 2.20462

zweight_in_kg = round(weight / lbs_in_kg)
zheight_in_cent = round(height * cent_in_inches)
print "Zed's weight in kilograms is %s." % zweight_in_kg
print "Zed's weight in centimeters is %s" % zheight_in_cent