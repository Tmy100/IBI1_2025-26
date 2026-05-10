#Count_codons
#Quantify the stop codon usage across genes containing that stop codons and generate a pie chart

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import re

#Ask user to input the stop codon
while True:
    user_stop = input("Please input one of the stop codons (eg. TAA/TAG/TGA): ").upper()
    if user_stop in ('TAA', 'TAG', 'TGA'):
        break
    else:
        print("Incorrect stop codon. Please try again.")

codon_counts = {}
current_seq = ""

#Read the fasta file that has been organised
with open('stop_genes.fa', 'r') as fasta_file:
    for line in fasta_file:
        line = line.strip()
        
        if line.startswith('>'):
            if current_seq != "":
                if user_stop in current_seq:
                    #Split at the stop codon, take the first part
                    extract_seq = current_seq.split(user_stop)[0]
                    
                    #Find all 3-letter chunks
                    codons = re.findall(r'.{3}', extract_seq)
                    for single_codon in codons:
                        if single_codon in codon_counts:
                            codon_counts[single_codon] += 1
                        else:
                            codon_counts[single_codon] = 1
                            
                    #Add the stop codon itself
                    if user_stop in codon_counts:
                        codon_counts[user_stop] += 1
                    else:
                        codon_counts[user_stop] = 1
                        
            #Reset the sequence to empty for the new gene
            current_seq = ""
            
        else:
            #This is a line of DNA. Add it to our sequence string.
            current_seq += line.upper()

#Catch the very last sequence in the file after the loop finishes
if current_seq != "" and user_stop in current_seq:
    extract_seq = current_seq.split(user_stop)[0]
    codons = re.findall(r'.{3}', extract_seq)
    for single_codon in codons:
        if single_codon in codon_counts:
            codon_counts[single_codon] += 1
        else:
            codon_counts[single_codon] = 1
    if user_stop in codon_counts:
        codon_counts[user_stop] += 1
    else:
        codon_counts[user_stop] = 1


#Ensures ONLY actual 3-letter DNA codons make it to the chart
valid_bases = set('ACGT')
final_counts = {}
for codon, count in codon_counts.items():
    if len(codon) == 3 and all(base in valid_bases for base in codon):
        final_counts[codon] = count

#Plot a pie chart
labels = list(final_counts.keys())
sizes = list(final_counts.values())

#If the stop codon doesn't exist
if len(labels) == 0:
    print(f"No data found for stop codon {user_stop}.")
else:
    plt.figure(figsize=(12, 7))
    colors = cm.rainbow(np.linspace(0, 1, len(labels)))
    wedges, texts = plt.pie(sizes, colors=colors, startangle=90, wedgeprops={'edgecolor': 'black', 'linewidth': 0.5})
    plt.legend(wedges, labels, title="Codons", loc="center left", bbox_to_anchor=(1, 0.5), ncol=2)
    plt.title(f"Distribution of Codons (Stop Codon: {user_stop})")
    plt.tight_layout()
    plt.show()