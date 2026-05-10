#Protein_mass_predictor
import re

def predict_protein_mass():
    '''
    Takes an amino acid sequence, returns the mass of the total protein in amu.
    Report error if amino acid not defined correctly and cannot be found.
    '''

    #{symbol, amu}
    dict ={ 'G':57.02, 
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
    
    while True: 
        input_name = input('Input the amino acid sequence (eg. GAV):')
                #Check if every amino acid entered is valid in our dictionary
        is_valid = True
        for amino_acid in input_name:
            if amino_acid not in dict:
                is_valid = False
                break #Stop checking once find an invalid one

        if is_valid:
            #Slice the sequence into a list like ['G','A','V']
            split_sequence = list(input_name) 
            
            # save the values into a list
            mass_values = []
            for aa in split_sequence:
                mass_values.append(dict[aa]) #Use dictionary to match keys to values
                
            #Sum them up
            total_mass = sum(mass_values)
            
            #Return the calculated value
            return total_mass

        #Else print error and ask to reinput the data
        else:
            print('Error: Amino acid or symbol not found. Please try again.') #Input the data to search
        
    
mass = predict_protein_mass()
print (f"The mass is {mass}")
    
