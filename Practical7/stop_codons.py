#open the file and output to a new fasta file
fasta_file= open('Saccharomyces_cerevisiae.R64-1-1.cdna.all (3).fa','r')
out_file= open('stop_genes.fa','w')
dict= {'TAA':'STOP','TGA':'STOP','TAG':'STOP'}
cDNA=''
#identify the ">", determine the start point
for line in fasta_file:
    if line[0:1] == '>':
        fields = line.split (' ')
        out_file.write (fields[0]+ ';' )
        if line[0:] == 'ATG':
            stop_codons = line.split ()[1].strip()
            out_file.write (stop_codons)
#identify the gene names and print
    elif not line.startswith ('>'):
        cDNA= cDNA + line.strip() #make the seq stick together
        out_file.write ('\n' + cDNA)

for frame in range (3):
    seq=''
    print ('Reading frame'+str(frame+1))
    for i in range (frame, len(cDNA),3):
        codon= cDNA[i:i +3]
        if codon in dict == 'STOP':
            out_file.write (';'+ seq) #identify the stopcodons and print
        else:
            out_file.write ('\n')
   
#3. output: {gene name}+_mRNA; {all in-frame stop codon}
#            /n {strip(seq)}
#4. create dict: stop codons= {TAA,TAG,TGA}
#5. identify and extract those need to shown in output using split.

