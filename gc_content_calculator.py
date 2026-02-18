# GC Content Calculator
# This script calculates the GC percentage of a DNA sequence.

user_dna = input("Enter a DNA sequence: ").upper()

sequence_length = len(user_dna)

if sequence_length == 0:
    print("No sequence entered.")
else:
    gc_count = user_dna.count("G") + user_dna.count("C")
    gc_content = (gc_count / sequence_length) * 100

    print(f"\nSequence length: {sequence_length}")
    print(f"GC count: {gc_count}")
    print(f"GC content: {gc_content:.2f}%")
