#print "How old are you?", 
#age = raw_input()
#print "How tall are you?",
#height = raw_input(); 
#print "How much do you weigh?",
#weight = raw_input(); 

#print "So you're %r years old, you are %r and you weigh %r" % (age, height, weight)

print "Let's calculate your BMI. How tall are you? Give your height in meters."
tall = float(raw_input())
print "What is your weight in kilograms?"
heavy = float(raw_input())
print "Your BMI is %f!" % (heavy / (tall * tall) ) 

