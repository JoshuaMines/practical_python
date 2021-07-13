current_movies = {'the grinch': "11:00am",
                  'rudolph': "12:00am",
                  'christmas': "3:00pm"}

print("we're showing the following movies:")
for key in current_movies:
    print(key)
movie = input("what movie would you like showtime for\n")

showtime = current_movies.get(movie)
if showtime == None:
    print('requested showtime isnt play')
else:
    print(movie, 'is playing at', showtime)