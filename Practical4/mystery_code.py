# What does this piece of code do?
# Answer: It will add up all the random numbers obtained in each round, and the final result is the sum of the random numbers obtained in all ten rounds.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n
	print(n)

print(total_rand)

#hypothesis: i tried print (n)
#result: it works.