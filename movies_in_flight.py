'''
You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

e.g.
Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250

Output from aonecode.com
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)
'''
def moviestowatch(movie, duration):
    target = duration - 30
    movie_duration = sorted(movie)
    i = 0
    j = len(movie_duration) - 1 
    max_duration = 0
    while i < j:
        if movie_duration[i] + movie_duration[j] <= target:
            if max_duration < movie_duration[i] + movie_duration[j]:
                max_duration = movie_duration[i] + movie_duration[j]
                first = i
                second = j
                #print(max_duration)
            i += 1
        else:
            j -=1
    #print(first,second)
    return movie_duration[first],movie_duration[second]

print(moviestowatch([90, 85, 75, 60, 120, 150, 125], 250))

