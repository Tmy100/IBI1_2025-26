#write	code	to	identify	the	longest	potential	open	reading	in within	gene	sequences.	
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

#Part1: Identify the largest Open Reading Frames and report the length of it
import re
longest_orf1= re.search ("^AUG.*UAA$",seq)
longest_orf2= re.search ("^AUG.*UAG$",seq)
longest_orf3= re.search ("^AUG.*UGA$", seq)

#if longest_orf1:
#    print (longest_orf1)
#elif longest_orf2:
#    print (longest_orf2)
#else:
#    print (longest_orf3)

print (longest_orf3)
print (longest_orf2)
print (longest_orf1)