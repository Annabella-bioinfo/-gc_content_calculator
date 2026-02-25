# GC Content Calculator

A Python tool that calculates the GC content of a DNA sequence with biological validation and input cleaning.


## What is GC Content?

GC content refers to the percentage of nucleotides in a DNA sequence that are either:

- **G (Guanine)**
- **C (Cytosine)**

GC-rich DNA regions are more thermally stable because G–C base pairs form three hydrogen bonds compared to two in A–T pairs.

GC content is commonly used in:

- Genome analysis  
- Comparing species  
- Sequencing quality assessment  
- Studying genomic stability  


This script:

- Accepts a DNA sequence from the user  
- Converts lowercase input to uppercase  
- Removes whitespace and newline characters  
- Validates biological bases (A, T, G, C, N)  
- Ignores invalid characters and reports them  
- Excludes ambiguous base **N** from GC percentage calculation  
- Prevents division-by-zero errors  
- Displays formatted analytical results  


## How It Works

The program follows three main steps:

1. **Clean the input**
   - Standardizes formatting.

2. **Validate the sequence**
   - Keeps only A, T, G, C, and N.
   - Detects and reports invalid characters.

3. **Calculate GC content**
   - Computes GC% using only valid A/T/G/C bases.
   - Excludes ambiguous bases (N).


## Example

**Input:**
ATGCGX12NN

**Output:**

--- Results ---
Valid DNA length (A/T/G/C only): 5
GC count: 3
AT count: 2
GC content: 60.00%

Warning: Invalid characters detected and ignored:
1, 2, X

## How to Run

1. Make sure Python is installed.
2. Run the script in your terminal:
   python gc_content.py

3. Enter a DNA sequence when prompted.

## Project Purpose

This project demonstrates:

- Basic bioinformatics computation  
- Biological data validation  
- Modular Python programming  
- Defensive programming practices
