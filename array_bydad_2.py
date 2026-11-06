def left_rotate(n):
    """
    arg
    n: the number of positions to rotate the array to the left.
    return: the array after left rotation by n positions.
    """
    gene_exp = [10, 25, 12, 40, 30]
    n = n % len(gene_exp)
    return gene_exp[n:] + gene_exp[:n]



print("left rotate(2)", left_rotate(2))