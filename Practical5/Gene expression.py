#Part1: Create and print a dictionary
gene_dict = {
    "TP53":12.4, 
    "EGFR":15.1, 
    "BRCA1":8.2, 
    "PTEN":5.3, 
    "ESR1":10.7 }  
print ("Initial gene dictionary:", gene_dict)


gene_dict ["MYC"] = 11.6 #adding new gene: MYC with 11.6
print ("Dictionary after adding MYC:", gene_dict)


# Part2: Test the gene of interest 
# Modify the variable 'gene_of_interest' below to search for a gene.
# Try setting it to 'BRCA1', 'MYC', or a fake gene like 'FAKEGENE'
gene_of_interest = 'Fakegene'

#Check if the gene is in the dictionary keys
if gene_of_interest in gene_dict:
    print(f"The expression value for {gene_of_interest} is: {gene_dict[gene_of_interest]}")
else:
    print(f"Error: The gene '{gene_of_interest}' is not present in the dataset.")
    
#Get all the values from the dictionary and calculate the average expression
all_values = gene_dict.values()
average_expression = sum(all_values) / len(all_values)

#Print the final statement (using round() to keep it to 2 decimal places for neatness)
print(f"The average gene expression level across all genes is: {round(average_expression, 2)}")


#Part3: Create bar chart
import matplotlib.pyplot as plt

#Extract the keys (gene names) and values (expression levels)
genes = list(gene_dict.keys())
expressions = list(gene_dict.values())

plt.bar(genes, expressions, color='skyblue', edgecolor='black')
plt.xlabel('Gene Name')
plt.ylabel('Expression Level')
plt.title('Gene Expression Levels in Biological Sample')

plt.show()