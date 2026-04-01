# Open Reading Frames (ORF)
# search the longest chain

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# search the start point AUG, no space, 3 as a group
# start codon begin at anywhere
import re
targets = ["AUG", "UAA", "UGA", "UAG"]

for codon in targets:
    match = re.search(f"({codon})", seq) 
    
    if match:
        print("Codon exist:",match)
    else:
        print("none\n") # create a newline (/n)

# UAA, UGA exist, but UAG doesn't exist

# Logic: find AUG, stop at UAG
#   if there is UAG, print the output
#	else run again and stop at UAA
#	else run again and stop at UGA

result_UAA = re.findall(r"AUG.*UAA", seq)

result_UGA = re.findall(r"AUG.*UGA", seq)

# If len(UGA) > len(UAA):
# print "largest:" (UGA) and len(UGA)
# else print UAA using same printing format.
[chain1]= result_UAA
[chain2]= result_UGA

if len(chain1) > len(chain2):
	print("longest:",chain1)
	print("length:", len(chain1))
else:
    print("longest:", chain2)
    print("length:", len(chain2))

