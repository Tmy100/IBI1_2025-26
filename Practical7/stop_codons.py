
"""
Yeast Stop Codon Usage Analyzer
Reads yeast cDNA FASTA file and counts stop codon usage per sequence
"""

import re
from collections import defaultdict

# Define stop codons
STOP_CODONS = {"TAA", "TAG", "TGA"}

def find_stop_codon(sequence, require_start=True):
    """
    Find the first stop codon in the sequence (in-frame)
    
    Parameters:
        sequence: DNA sequence string
        require_start: If True, start reading from the first ATG
    
    Returns:
        Stop codon (TAA/TAG/TGA) or None
    """
    seq_upper = sequence.upper()
    
    # Locate start codon (optional)
    start_pos = 0
    if require_start:
        start_idx = seq_upper.find("ATG")
        if start_idx == -1:
            return None  # No start codon, skip
        start_pos = start_idx
    
    # Scan in steps of 3 from start position
    for i in range(start_pos, len(seq_upper) - 2, 3):
        codon = seq_upper[i:i+3]
        if codon in STOP_CODONS:
            return codon
    
    return None

def parse_fasta(file_path):
    """
    Parse FASTA file, yield (header, sequence) pairs
    """
    with open(file_path, 'r') as f:
        header = None
        seq_lines = []
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('>'):
                # Save previous sequence
                if header is not None:
                    yield header, ''.join(seq_lines)
                # Start new sequence
                header = line
                seq_lines = []
            else:
                # Accumulate sequence lines
                seq_lines.append(line)
        
        # Last sequence
        if header is not None:
            yield header, ''.join(seq_lines)

def analyze_stop_codons(fasta_file, require_start=True):
    """
    Analyze stop codon usage in all sequences in FASTA file
    """
    counts = defaultdict(int)
    total_sequences = 0
    sequences_with_stop = 0
    results = []  # Store (header, stop_codon) for each sequence
    
    for header, sequence in parse_fasta(fasta_file):
        total_sequences += 1
        stop_codon = find_stop_codon(sequence, require_start)
        
        if stop_codon:
            counts[stop_codon] += 1
            sequences_with_stop += 1
            # Extract sequence name (remove '>')
            seq_name = header[1:].split()[0] if header.startswith('>') else header
            results.append((seq_name, stop_codon))
    
    return {
        'total_sequences': total_sequences,
        'sequences_with_stop': sequences_with_stop,
        'counts': dict(counts),
        'results': results
    }

def print_results(stats):
    """Print statistics"""
    print("=" * 50)
    print("Yeast cDNA Stop Codon Usage Statistics")
    print("=" * 50)
    print(f"Total sequences: {stats['total_sequences']}")
    print(f"Sequences with stop codon: {stats['sequences_with_stop']}")
    print(f"Sequences without start or stop codon: {stats['total_sequences'] - stats['sequences_with_stop']}")
    print("\nStop codon counts:")
    for codon in ["TAA", "TAG", "TGA"]:
        count = stats['counts'].get(codon, 0)
        print(f"  {codon}: {count}")
    
    # Calculate percentages
    if stats['sequences_with_stop'] > 0:
        print("\nStop codon percentages:")
        for codon in ["TAA", "TAG", "TGA"]:
            count = stats['counts'].get(codon, 0)
            pct = (count / stats['sequences_with_stop']) * 100
            print(f"  {codon}: {pct:.2f}%")

def save_detailed_results(stats, output_file="stop_codon_results.txt"):
    """Save detailed results to file (format: >sequence_name;stop_codon)"""
    with open(output_file, 'w') as f:
        for seq_name, stop_codon in stats['results']:
            f.write(f">{seq_name};{stop_codon}\n")
    print(f"\nDetailed results saved to: {output_file}")

def main():
    # Set your FASTA file path here
    fasta_file = Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.gz  # Replace with actual path
    
    try:
        # Analyze stop codons (require reading frame from ATG)
        stats = analyze_stop_codons(fasta_file, require_start=True)
        
        # Print results
        print_results(stats)
        
        # Save detailed results
        save_detailed_results(stats)
        
        # Optional: Print first 10 results as example
        print("\nFirst 10 sequences example:")
        for seq_name, stop in stats['results'][:10]:
            print(f"  >{seq_name};{stop}")
    
    except FileNotFoundError:
        print(f"Error: File '{fasta_file}' not found")
        print("Please ensure the file path is correct, or modify the fasta_file variable in main()")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()