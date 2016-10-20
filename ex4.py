#Assigns how many cars we have to variable cars
cars = 100
#assigns how many people can fit in one car to variable space_in_a_car
space_in_a_car = 4.0
#how many drivers assgned to drivers
drivers = 30
#total number of passengers assigned to passengers
passengers = 90
#calculates number of cars without drivers by subtracting cars from cars_not_driven
cars_not_driven = cars - drivers
#sets number of cars driven equa to the number of drivers
cars_driven = drivers
#total capacity of the carpool derived from multiplyng cars_driven by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#calculates avg amount of passengers per car needed to drive all passengers
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#carpool should be one word so when the program runs car_pool relates
#to a new variable that is not assigned

#if you use 4 instead of 4.0 you get the same result because it just so happens
#divide into an integer value but it might still be good practice for more accuracy
#to use floating point