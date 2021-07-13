temperature = 75
forecast = 'rain'
raining = False

if temperature > 80:
    print("its too hot")
    print("stay inside!")
elif temperature < 60:
    print("shit is cold \n stay inside")
else: 
    print("enjoy the outdoors")

#or lets us combine comaprisions
if temperature < 50 or temperature > 90: 
    print("stay inside")
else: 
    print("you can go out")

#and lets us combine comaprisions 
if temperature < 60 and forecast == 'rain':
    print('stay inside')
else:
    print('go outside')

#not lets us negate comparison
if not forecast == 'rain':
    print("go outside")
else:
    print("stay inside")

if raining:
    print("go outside")\

else:
    print("stay insde")