def reverse(dna_strand):
    """
    arg 
    n: the number of elements in the list to be reversed.
    return: the reversed list of elements from 1 to n.
    """
    n = len(dna_strand)
    i = 0 # index of the first element in the list
    j = n-1 # index of the last element in the list

    while i < j:
        dna_strand[i], dna_strand[j] = dna_strand[j], dna_strand[i]
        i += 1
        j -= 1

    return dna_strand

dna = ['A', 'T', 'G', 'C', 'C', 'A']
reversed_dna_strand = reverse(dna)
print(reversed_dna_strand)