
age = int(input("how old are you?\n")) #input() asks for a response

decades = age // 10 #// rounds number to an integer.  one / makes it a float
years = age % 10 # % modulous returns leftover after division

print("you are " + str(decades) + " decades and" + str(years) + " syears old")