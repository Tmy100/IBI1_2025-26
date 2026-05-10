#Largest_orf
#Identify they largest ORF and its nucleotide length.

import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAAG'
stop_codons = ["UAA", "UGA", "UAG"]

#Store all found chains in a list
all_found_chains = []


for stop in stop_codons:
    #greedy search
    pattern = f"AUG.*{stop}"
    matches = re.findall(pattern, seq)
    
    #find for all stop codons that existing in the seq
    if matches:
        print(f"Stop codon '{stop}' do exist")
        all_found_chains.extend(matches) #save the existed chains into the list
    else:
        print(f"Stop codon '{stop}' doesn't exist")

#determine the longest chain
if len(all_found_chains) > 0:
    
    longest_chain = max(all_found_chains, key=len)
    
    print("\nThe longest chain:", longest_chain)
    print("The length of the chain:", len(longest_chain), "nucleotides")
else:
    print("There is not a complete chain exist.")