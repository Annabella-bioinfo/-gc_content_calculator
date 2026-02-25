def clean_sequence(sequence):
    """
    Cleans the input DNA sequence:
    - Converts to uppercase
    - Removes whitespace and newline characters
    """
    sequence = sequence.upper()
    sequence = sequence.replace(" ", "")
    sequence = sequence.replace("\n", "")
    return sequence


def validate_sequence(sequence):
    """
    Validates the DNA sequence.
    Returns:
    - cleaned valid sequence (A, T, G, C, N only)
    - list of invalid characters found
    """
    valid_bases = {"A", "T", "G", "C", "N"}
    cleaned_sequence = ""
    invalid_characters = set()

    for base in sequence:
        if base in valid_bases:
            cleaned_sequence += base
        else:
            invalid_characters.add(base)

    return cleaned_sequence, invalid_characters


def calculate_gc_content(sequence):
    """
    Calculates GC content excluding ambiguous base 'N'
    """
    gc_count = sequence.count("G") + sequence.count("C")
    at_count = sequence.count("A") + sequence.count("T")

    valid_length = gc_count + at_count  # Excludes N

    if valid_length == 0:
        return 0, gc_count, at_count, valid_length

    gc_content = (gc_count / valid_length) * 100
    return gc_content, gc_count, at_count, valid_length


# -------- Main Program --------

user_input = input("Enter DNA sequence: ")

# Step 1: Clean
cleaned = clean_sequence(user_input)

# Step 2: Validate
validated_sequence, invalid_chars = validate_sequence(cleaned)

# Step 3: Calculate GC
gc_content, gc_count, at_count, valid_length = calculate_gc_content(validated_sequence)

# Output Results
print("\n--- Results ---")
print(f"Valid DNA length (A/T/G/C only): {valid_length}")
print(f"GC count: {gc_count}")
print(f"AT count: {at_count}")
print(f"GC content: {gc_content:.2f}%")

# Warning for invalid characters
if invalid_chars:
    print("\nWarning: Invalid characters detected and ignored:")
    print(", ".join(sorted(invalid_chars)))
