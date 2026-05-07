#Protein mass predictor
def predict_protein_mass():
    '''
    Takes an amino acid sequence, returns the mass of the total protein in amu.
    Report error if amino acid not defined correctly and cannot be found.
    '''
    #0. create a dictionary {aminoacid,amu}
    dict1 ={ 'Glycine':57.02, 
            'Alanine':71.04,
            'Serine':87.03,
            'Proline':97.05, 
            'Valine':99.07,
            'Threonine':101.05,
            'Cysteine':103.01,
            'Isoleucine':113.08,
            'Leucine':113.08,
            'Asparagine':114.04,
            'Aspartic Acid':115.03,
            'Glutamine':128.06,
            'Lysine':128.09,
            'Glutamic Acid':129.04,
            'Methionine':131.04,
            'Histidine':137.06,
            'Phenylalanine':147.07,
            'Arginine':156.10,
            'Tyrosine':163.06,
            'Tryptophan':186.08}
    
    # {symbol, amu}
    dict2 ={ 'G':57.02, 
            'A':71.04,
            'S':87.03,
            'P':97.05, 
            'V':99.07,
            'T':101.05,
            'C':103.01,
            'I':113.08,
            'L':113.08,
            'N':114.04,
            'D':115.03,
            'Q':128.06,
            'K':128.09,
            'E':129.04,
            'M':131.04,
            'H':137.06,
            'F':147.07,
            'R':156.10,
            'Y':163.06,
            'W':186.08}
    
        # Use loop to ask user reinput if there is an error.
    while True: 
    #1. input the data to search
                input_name = input('Input the name of amino acid or the symbol (eg. Alanine/A):')

    #2. check validity
                if input_name in dict1: 
                        return dict1[input_name]
    
                elif input_name in dict2:
                        return dict2[input_name]
    
                else:
                        print ('Error: Amino acid or symbol not found. Please try again.')
    
    # if input_name can be found in both dict, print the according amu
    # else print error and ask to reinput the data
                             

mass = predict_protein_mass()
print (f"The mass is {mass}")
    
