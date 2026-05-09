#open the file
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import re

while True:
    #ask user to input
    user_input= input("Please input one of the the stop codons (eg. TAA/TAG/TGA)")

    if user_input in ('TAA','TAG','TGA'):
         break
    else: print("Incorrect stop codon. Please try again.")

current_seq=""
codon_counts= {}

with open('stop_genes.fa', 'r') as fasta_file:
    #calculate totals of all possible in-frame stop codons.
        for line in fasta_file:
            line= line.strip ()

            if line.startswith('>'):
                if current_seq != "":  
                    
                    if user_input in current_seq:
                        #1.calculate the amount of codons before the input stop codons
                        #split the last codon
                        codon=line.split(user_input)
                        #split the alphabets of 3 into a group 
                        extract_seq= codon[0]
                        #codons= re.split(r'\S..',extract_seq) is wrong
                        codons= re.findall(r'.{3}', extract_seq)
                        #calculate the number of codons
                        count_codons= len(codons)
                        print("The total counts of possible in-frame codons:", count_codons)

                        #2. categorise each codons into a different group (eg. ATG, TAA), include the input stop codon
                        # Loop through the list of extracted codons (the value)
                        for single_codon in codons:
                             # If we've seen this codon before, add 1 to its count
                            if single_codon in codon_counts:
                                codon_counts[single_codon] += 1
                            # If it's the first time seeing it, set its count to 1
                            else:
                                codon_counts[single_codon] = 1
                
                            # The comment asks to also include the input stop codon in the count (the key)
                        if input in codon_counts:
                            codon_counts[input] += 1
                        else:
                            codon_counts[input] = 1
                current_seq=""
            else:
                current_seq += line
                    #Create a pie chart of the codons distribution.

labels= list(codon_counts.keys())
sizes= list(codon_counts.values())
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title(f"Distribution of Codons (Stop Codon:{user_input})")
plt.show()

print("Processing complete.")