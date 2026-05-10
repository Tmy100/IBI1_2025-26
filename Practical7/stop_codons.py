#Stop_codons
#Read a fasta file and output the gene names, the stop codons found and the gene's cDNA sequence into a fasta file

stop_codons = ['TAA', 'TGA', 'TAG']

#Read and write the file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all (3).fa', 'r') as fasta_file, \
     open('stop_genes.fa', 'w') as out_file:
    
    current_gene_id = ""
    current_seq = ""
    
    for line in fasta_file:
        line = line.strip() #Make the seq stick together as a longchain
        
        #Identify the marker ">" and start reading
        if line.startswith('>'):
            #Check if there is a complete seq, else end.
            if current_seq != "":
                
                #Store the stop codons that were found in a list
                found_codons = []
                
                #Check if the stop codons existed in the seq
                for codon in stop_codons:
                    if codon in current_seq:  
                        found_codons.append(codon)
                
                #If there is more than one stop codons, print them out
                if len(found_codons) > 0:
                    codons_str = ",".join(found_codons)
                    new_header = f"{current_gene_id}_{codons_str}"

                #If there are no stop codons existed, only print the gene name
                else:
                    new_header = f"{current_gene_id}" 
                
                #Write the new header and seq into the output file
                out_file.write(f"{new_header}\n")
                out_file.write(f"{current_seq}\n")

            #(Repeat) Search for a new gene and reset everything
            fields = line.split(' ')
            current_gene_id = fields[0]
            current_seq = ""
            
        #If it is a seq data, accumulate the line
        else:
            current_seq += line

    #Process the last gene
    if current_seq != "":
        found_codons = []
        for codon in stop_codons:
            if codon in current_seq:
                found_codons.append(codon)
        
        if len(found_codons) > 0:
            codons_str = "_".join(found_codons)
            new_header = f"{current_gene_id}_{codons_str}"
        else:
            new_header = f"{current_gene_id}"
            
        out_file.write(f"{new_header}\n")
        out_file.write(f"{current_seq}\n")

print("Processing complete. Check stop_genes.fa")